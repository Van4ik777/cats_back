# 🎉 Event Management API

A Django REST API to manage events (conferences, meetups, etc.).

## 🚀 Features

- User registration and authentication (with email confirmation)
- CRUD operations for events
- Filtering and search support
- Event registration logic
- API docs via Swagger
- Dockerized

---

## 🐳 Run with Docker

### 1. Clone and configure

```bash
git clone <your-repo-url>
cd your-project
cp .env.example .env
docker compose build
docker compose up
docker exec -it crud_sv-web-1 python src/manage.py makemigrations
docker exec -it crud_sv-web-1 python src/manage.py migrate

