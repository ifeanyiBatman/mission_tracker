## User Flow / Routes
- Home
- Create mission
- Edit mission
- Delete mission
- Create Brain Dump
- Signup, Login , Logout , JWTtokens

## Logic


## Templates

## User stories:
- as a signed in user , i want to see missions , so i can complete them.
- as a signed in user , i want to be able to create new missions.
- as a signed in user , i want to be able to edit missions with new info.
- as a signed in user , i want to be able to mark missions as complete.
- as a signed in user , i want to be able to view my dumps.
- as a signed in user , i want to be able to create new dumps.
- as a signed in user , i want to be see and track my xp.
- as a user i want to be able to signup.
- as a user i want to be able to login.
- as a user i want to be able to log out.


## API ROUTES and Models
### API ROUTES
- [x] GET  "/" - returns the index page.
- [x] GET "/missions" - returns the content for the missions
- [x] POST "/missions" - create a new mission.
- [x] PATCH "/missions/{mission_id}" - edit a mission.
- [x] POST "/missions/{mission_id}/complete" - mark a mission as complete.
- [x] GET "/dumps" - renders the list of dumps.
- [x] POST "/dumps" - create a new dump.
- POST "/dumps/{dump_id}/archive" - archive a dump

### MODELS
- MISSION : {
    id: int,
    title: str'
    start_date: datetime,
    end_date: datetime,
    is_daily_habit: bool,
    xp: int
    user_id: int
}
- DUMP : {
    id: int,
    content: str,
    dumped: datetime,
    is_archived: bool,
    user_id: str
}
- USER {
    id: int,
    username: str
    email: str,
    password: str,
    xp: int,
    level: int,
    created_at: datetime,
    updated_at: datetime
}
