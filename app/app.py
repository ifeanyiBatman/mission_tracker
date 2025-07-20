from fastapi import FastAPI, Request , Form
from fastapi.templating import Jinja2Templates
import app.data as data
from typing import Annotated
import datetime
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles # Added import

missions = data.MISSIONS
dumps = data.DUMPS
current_user = data.USERS[0]
next_mission_id = 3
completed_missions = [1]
next_dump_id = 10


class DumpEntryCreate(BaseModel):
    content: str
    dumped: datetime.datetime
    is_archived : bool = False
    user_id: int = current_user['id']

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static") # Added static files mount


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
    return templates.TemplateResponse("index.html", {"request": request, "user": user, "missions": users_missions, "dumps": users_dumps, "completed": completed_missions})

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
    return templates.TemplateResponse("mission.html", {"request": request, "mission": new_mission})

@app.get("/missions/{mission_id}/edit")
async def get_mission_edit_form(request: Request, mission_id:int ):
    edit_mission = {}
    for mission in missions:
        if mission_id == mission["id"]:
            edit_mission = mission
    return templates.TemplateResponse("mission-edit.html", {"request":request, "mission": edit_mission })

@app.get("/missions/{mission_id}")
async def get_single_mission(request:Request, mission_id:int):
    found_mission = None
    for mission in missions:
        if mission_id == mission["id"]:
            found_mission = mission
    return templates.TemplateResponse("mission.html",{"request":request , "mission":found_mission})

@app.patch("/missions/{mission_id}")
async def update_mission(
    request: Request,
    mission_id: int ,
    mission: Annotated[str,Form()],
    xp: Annotated[int,Form()],
    tags: Annotated[str,Form()],
    start: Annotated[str,Form()], # You might want to convert this to a date object later
    end: Annotated[str,Form()],   # You might want to convert this to a date object later
    habit: Annotated[str,Form()] ):

    updated_mission = {}
    for item in missions:
        if item["id"] == mission_id:
            updated_mission = item
    if habit == "Habit":
        habitBool = True
    else:
        habitBool = False

    if mission is not None:
        updated_mission["title"] = mission
    if start is not None:
        updated_mission["start_date"] = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M')
    if end is not None:
        updated_mission["end_date"] = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M')
    if habit is not None:
        updated_mission["is_daily_habit"] = habitBool
    if xp is not None:
        updated_mission["xp"] = xp
    return templates.TemplateResponse("mission.html",{"request":request, "mission": updated_mission})

@app.post("/missions/{mission_id}/complete")
async def complete_mission(request:Request, mission_id: int):
    completed_mission = {}
    for mission in missions:
        if mission["id"] == mission_id:
            completed_mission = mission
    if mission_id not in completed_missions:
        current_user["xp"] += completed_mission["xp"]
        completed_missions.append(mission_id)
    return templates.TemplateResponse("complete.html",{"request":request})

@app.post("/dumps")
async def create_new_dump(request:Request,dump:Annotated[str,Form()]):
    global next_dump_id
    new_dump = {
        "id":next_dump_id,
        "content": dump,
        "dumped": datetime.datetime.now(),
        "is_archived": False,
        "user_id": current_user["id"]
    }
    dumps.append(new_dump)
    next_dump_id += 1
    return templates.TemplateResponse("dump.html",{"request":request,"dump" : new_dump })




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
