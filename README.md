# Hello World API: Django + Python Sample

This repository contains a Django project that defines an REST Framework API. You'll secure this API with Auth0 to practice making secure API calls from a client application.

## Get Started

Prerequisites:
    
* Python >= 3.6

Initialize a python virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run DB migrations:

```bash
python manage.py migrate
```

Run the project in dev mode:

```bash
python manage.py runserver 6060
```

## API Endpoints

### 🔓 Get public message

```bash
GET /api/messages/public
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API doesn't require an access token to share this message."
}
```

### 🔓 Get protected message

> You need to protect this endpoint using Auth0.

```bash
GET /api/messages/protected
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API successfully validated your access token."
}
```

### 🔓 Get admin message

> You need to protect this endpoint using Auth0 and Role-Based Access Control (RBAC).

```bash
GET /api/messages/admin
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API successfully recognized you as an admin."
}
```