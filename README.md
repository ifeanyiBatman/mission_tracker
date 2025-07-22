# Mission Tracker (Work in Progress)

**Mission Tracker** is a simple web app I’m building for myself. The idea is to have a clean place to log daily routines, track missions (tasks or goals), and drop brain dumps—random thoughts, ideas, or fragments—without getting lost in over-complicated tools like Obsidian or Notion.

I haven’t started using it yet. Still working on the layout, behavior, and deciding what’s essential. There’s no storage right now—everything is in-memory, so data resets every time the app is restarted.

## Why I’m Building It

I got tired of setting up and maintaining heavy productivity apps just to write down things I need to get done. I needed something that’s:

* Local and fast
* Easy to add a task or idea without thinking
* Focused on just me—no user accounts, no sync, no distractions

## What It Can Do (So Far)

* Add a mission (something I need to do)
* Mark a mission as complete
* Write and edit a brain dump—just freeform notes
* View everything on one simple page

## What It’s Built With

* FastAPI for the backend
* HTMX for frontend interactivity (no React or JS frameworks)
* No database yet—just in-memory lists
* Runs locally with `uvicorn`

## How to Run It (Development Only)

```
git clone https://github.com/yourusername/mission-tracker.git
cd mission-tracker
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open your browser and go to:
`http://localhost:8000`

## What’s Missing (Planned but not built)

* Storage (probably SQLite or a simple file-based system)
* Mobile layout
* Markdown support for brain dumps
* Grouping or filtering missions by day or tag
* Maybe Git-based export for versioning

## Status

Still in the early stage. It runs, but I’m not using it daily yet. Just laying the foundation and getting the structure right before I commit to integrating it into my workflow.
