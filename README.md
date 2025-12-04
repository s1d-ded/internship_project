# internship_project
My internship project for the internship done at JBIET by me on back-end development basics, the domain is fomrula1 racing
# read.me
# 🏎️ F1 Backend Project (FastAPI)

## 📘 Overview
The **F1 Backend Project** is a RESTful API built with **FastAPI** to manage Formula 1 data — including **drivers**, **teams**, and **races**.  
It supports CRUD operations, data persistence via JSON or a database, and automatic API documentation through Swagger UI.
---
## ⚙️ Requirements
Before running the project, make sure you have:
- **Python 3.10 or newer**
- **pip** (Python package manager)
- Optionally, **virtual environment (venv)** for clean dependency management
---
## 📁 Directory Structure
Your project should follow this structure:
F1_Backend/
│
├── main.py # Entry point of the FastAPI app
├── db.py # Handles file or database connections
├── data.json # Local data storage (temporary database)
│
├── models/ # Contains Pydantic models (optional)
│ ├── driver.py
│ ├── team.py
│ └── race.py
│
├── schemas/ # Data validation & request/response schemas
│ ├── driver_schema.py
│ ├── team_schema.py
│ └── race_schema.py
│
├── routes/ # Routers for modular API endpoints
│ ├── driver.py
│ ├── team.py
│ └── race.py
│
├── services/ # Business logic layer (optional)
│ ├── driver_service.py
│ ├── team_service.py
│ └── race_service.py
Make sure the data inside db.json file is in this format
{
  "drivers": [],
  "teams": [],
  "races": []
}
Clone and download the repository to run the backend in either thunder client or swagger UI, create a venv environment to run(completely optional).
##pip install
pip install fastapi uvicorn pydantic typing-extensions python-multipart
//download these dependencies first



