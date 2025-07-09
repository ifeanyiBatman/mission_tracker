from fastapi import FastAPI, Request , Form
from fastapi.templating import Jinja2Templates
import app.data as data
from typing import Annotated
import datetime


missions = data.MISSIONS
dumps = data.DUMPS
current_user = data.USERS[0]
next_mission_id = 3

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    users_missions = []
    users_dumps = []
    user = current_user
    for mission in missions:
        if mission["user_id"] == user["id"]:
            users_missions.append(mission)
    for dump in dumps:
        if dump["user_id"] == user["id"]:
            users_dumps.append(dump)
    return templates.TemplateResponse("index.html", {"request": request, "user": user, "missions": users_missions, "dumps": users_dumps})

@app.post("/missions")
async def create_mission(
    request: Request,
    mission: Annotated[str,Form()],
    xp: Annotated[int,Form()],
    tags: Annotated[str,Form()],
    start: Annotated[str,Form()], # You might want to convert this to a date object later
    end: Annotated[str,Form()],   # You might want to convert this to a date object later
    habit: Annotated[str,Form()]):
    user = current_user
    global next_mission_id
    if habit== "Habit":
        habitBool = True
    else:
        habitBool = False
    new_mission = {
        "id": next_mission_id,
        "title": mission,
        "start_date": datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M'),
        "end_date": datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M'),
        "is_daily_habit": habitBool,
        "xp": xp,
        "user_id": user["id"]
    }
    missions.append(new_mission)
    next_mission_id += 1
    print("missions submitted \n")
    print(missions)
    return templates.TemplateResponse("mission.html", {"request": request, "mission": new_mission})
