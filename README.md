#🕵️‍♂️ Spy Cats API
A RESTful API for managing spy cats, their missions, and targets. Built with Django REST Framework and integrated with TheCatAPI for breed validation.

#🚀 Features
-Full CRUD for Spy Cats
-Assign missions to cats
-Track targets within missions
-Mark missions and targets as completed
-Validate cat breed via TheCatAPI

📦 Installation

```bash
git clone https://github.com/yourusername/spy-cats-api.git
cd spy-cats-api
docker compose build
docker compose up
docker exec -it crud_sv-web-1 python src/manage.py makemigrations
docker exec -it crud_sv-web-1 python src/manage.py migrate
```

## 🔌 API Endpoints

| Method | Endpoint                                    | Description                                  |
|--------|---------------------------------------------|----------------------------------------------|
| GET    | `/api/spy-cats/`                            | Retrieve all spy cats                        |
| POST   | `/api/spy-cats/`                            | Create a new spy cat                         |
| PATCH  | `/api/spy-cats/<id>/`                       | Update a spy cat                             |
| DELETE | `/api/spy-cats/<id>/`                       | Delete a spy cat                             |
| GET    | `/api/missions/`                            | Retrieve all missions                        |
| POST   | `/api/missions/`                            | Create a mission with targets                |
| POST   | `/api/missions/<id>/assign_cat/`            | Assign a cat to a mission                    |
| DELETE | `/api/missions/<id>/`                       | Delete a mission (only if no cat assigned)   |
| GET    | `/api/targets/`                             | Retrieve all targets                         |
| PATCH  | `/api/targets/<id>/`                        | Update a target                              |
| POST   | `/api/targets/<id>/mark_complete/`          | Mark a target as completed           
