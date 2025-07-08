from datetime import datetime

# In-memory lists to simulate database tables
# These lists will hold dictionaries representing the data models.

MISSIONS = [
    {
        "id": 1,
        "title": "Complete Project Proposal",
        "start_date": datetime(2023, 11, 27, 9, 0, 0),
        "end_date": datetime(2023, 11, 27, 17, 0, 0),
        "is_daily_habit": False,
        "xp": 150,
        "user_id": 1
    },
    {
        "id": 2,
        "title": "Daily Code Review (30 mins)",
        "start_date": datetime(2023, 11, 27, 10, 30, 0),
        "end_date": datetime(2023, 11, 27, 11, 0, 0),
        "is_daily_habit": True,
        "xp": 20,
        "user_id": 1
    },
    {
        "id": 3,
        "title": "Research New API Integrations",
        "start_date": datetime(2023, 11, 28, 9, 0, 0),
        "end_date": datetime(2023, 11, 29, 12, 0, 0),
        "is_daily_habit": False,
        "xp": 100,
        "user_id": 2
    },
    {
        "id": 4,
        "title": "Exercise (45 mins)",
        "start_date": datetime(2023, 11, 27, 18, 0, 0),
        "end_date": datetime(2023, 11, 27, 18, 45, 0),
        "is_daily_habit": True,
        "xp": 30,
        "user_id": 3
    }
]

DUMPS = [
    {
        "id": 1,
        "content": "Future feature idea: recurring missions with custom intervals.",
        "dumped": datetime(2023, 11, 26, 11, 15, 0),
        "is_archived": False,
        "user_id": 1
    },
    {
        "id": 2,
        "content": "Potential UI/UX improvements for mission list view: drag-and-drop reordering.",
        "dumped": datetime(2023, 11, 25, 16, 0, 0),
        "is_archived": False,
        "user_id": 2
    },
    {
        "id": 3,
        "content": "Consider adding achievements based on total XP or completed missions.",
        "dumped": datetime(2023, 11, 24, 9, 45, 0),
        "is_archived": False,
        "user_id": 1
    },
    {
        "id": 4,
        "content": "Need to research pagination for dump list for performance.",
        "dumped": datetime(2023, 11, 27, 13, 0, 0),
        "is_archived": False,
        "user_id": 3
    }
]

USERS = [
    {
        "id": 1,
        "username": "coder_king",
        "email": "coder.king@example.com",
        "password": "hashedpassword123", # Placeholder, in a real app this would be truly hashed
        "xp": 350,
        "level": 3,
        "created_at": datetime(2023, 10, 10, 8, 0, 0),
        "updated_at": datetime(2023, 11, 27, 17, 30, 0)
    },
    {
        "id": 2,
        "username": "dev_queen",
        "email": "dev.queen@example.com",
        "password": "hashedpassword456",
        "xp": 180,
        "level": 2,
        "created_at": datetime(2023, 10, 20, 9, 0, 0),
        "updated_at": datetime(2023, 11, 26, 10, 0, 0)
    },
    {
        "id": 3,
        "username": "tester_hero",
        "email": "tester.hero@example.com",
        "password": "hashedpassword789",
        "xp": 50,
        "level": 1,
        "created_at": datetime(2023, 11, 1, 10, 0, 0),
        "updated_at": datetime(2023, 11, 27, 18, 50, 0)
    }
]
