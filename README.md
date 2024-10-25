# SpyCat

# Technological stack
- FastAPI
- RESTful API
- SQLite
- Pydantic
- HTTPX
- SQLAlchemy
- Uvicorn

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd SpyCat
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix/Mac
   venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Running the Application
To start the FastAPI server with auto-reload for development:
```bash
uvicorn app.main:app --reload
```
# Requests:
### SpyCats
- Get a list of all SpyCats<br>
GET api/cats/<br>
<br>
- Create a new SpyCat<br>
POST api/cats/<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"name": "Name",<br>
&nbsp;&nbsp;&nbsp;"years_of_experience": 3,<br>
&nbsp;&nbsp;&nbsp;"breed": "Siamese",<br>
&nbsp;&nbsp;&nbsp;"salary": 5000<br>
}<br>
<br>
- Retrieve a SpyCat<br>
GET api/cats/{spy_cat_id}<br>
<br>
- Update SpyCat<br>
PUT api/cats/{spy_cat_id}<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"name": "Name",<br>
&nbsp;&nbsp;&nbsp;"years_of_experience": 3,<br>
&nbsp;&nbsp;&nbsp;"breed": "Siamese",<br>
&nbsp;&nbsp;&nbsp;"salary": 5000<br>
}<br>
<br>
- Delete SpyCat<br>
DELETE /api/cats/{spy_cat_id}<br>

### Missions
- Get a list of all missions<br>
GET api/missions/<br>
<br>
- Create a new mission<br>
POST api/missions/<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"cat_id": 1,<br>
&nbsp;&nbsp;&nbsp;"complete": false,<br>
&nbsp;&nbsp;&nbsp;"targets": ["Target Alpha", "Target Bravo"]<br>
}<br>
<br>
- Retrieve a mission<br>
GET api/missions/{mission_id}<br>
<br>
- Update mission<br>
PUT api/missions/{mission_id}<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"cat_id": 1,<br>
&nbsp;&nbsp;&nbsp;"complete": true,<br>
&nbsp;&nbsp;&nbsp;"targets": ["New Target Alpha", "New Target Delta"]<br>
}<br>
<br>
- Delete mission<br>
DELETE /api/missions/{mission_id}<br>

### Targets
- Get a list of all targets<br>
GET api/targets/<br>
<br>
- Create a new target<br>
POST api/targets/<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"name": "Target Alpha",<br>
&nbsp;&nbsp;&nbsp;"country": "CountryName",<br>
&nbsp;&nbsp;&nbsp;"notes": "This is a high-priority target."<br>
&nbsp;&nbsp;&nbsp;"complete": false,<br>
&nbsp;&nbsp;&nbsp;"mission_id": 1,<br>
}<br>
<br>
- Update target<br>
PUT api/targets/{target_id}<br>
Content-Type: application/json<br>
{<br>
&nbsp;&nbsp;&nbsp;"name": "Target Alpha",<br>
&nbsp;&nbsp;&nbsp;"country": "CountryName",<br>
&nbsp;&nbsp;&nbsp;"notes": "This is a high-priority target."<br>
&nbsp;&nbsp;&nbsp;"complete": false,<br>
&nbsp;&nbsp;&nbsp;"mission_id": 1,<br>
}<br>
<br>
- Delete target<br>
DELETE /api/targets/{target_id}<br>

## Developer
Sviatoslav Baranetskyi

Email: svyatoslav.baranetskiy738@gmail.com
