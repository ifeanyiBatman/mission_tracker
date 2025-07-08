from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import app.data as data
#from typing import Annotated

missions = data.MISSIONS
dumps = data.DUMPS
current_user = data.USERS[0]

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
