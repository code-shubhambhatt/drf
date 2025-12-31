# WatchMate API

WatchMate is a backend service built using Django and Django REST Framework for managing streaming platforms, watchlists, and user-generated reviews.

The system exposes clean, RESTful APIs designed with scalability, correctness, and maintainability in mind. It models real-world relationships between platforms, content, and users, and enforces data integrity through validation and constraints at the application layer.

---

## Overview

The API enables clients to:
- Manage streaming platforms
- Manage watchlists (movies or shows)
- Allow authenticated users to submit and manage reviews
- Retrieve structured, relational data through REST endpoints

The project follows service-oriented design principles and clean separation of concerns between models, serializers, views, and routing.

---

## Technology Stack

- **Language**: Python
- **Framework**: Django, Django REST Framework
- **Database**: SQLite (development), PostgreSQL-compatible
- **Architecture**:
  - APIView
  - Generic class-based views
  - ModelViewSet
- **Authentication Model**: Django built-in User model
- **Environment**: Linux / macOS / Windows

---

## Key Features

- RESTful CRUD APIs for streaming platforms
- RESTful CRUD APIs for watchlists
- User-based review system with:
  - Rating validation (1–5)
  - One-review-per-user-per-watchlist constraint
- Nested resource representation (watchlists with reviews)
- Proper HTTP status handling and error responses
- Extensible architecture suitable for additional services

---

## System Architecture

```

Client Applications
↓
REST API Layer (DRF)
↓
Business Logic & Validation
↓
Relational Data Models
↓
Database

````

The design supports extension for:
- Authentication tokens
- Rate limiting
- Caching
- Horizontal scaling behind load balancers

---

## Data Models

### StreamPlatform
Represents a streaming service provider.
- `name`
- `about`
- `website`

### WatchList
Represents a movie or show available on a platform.
- `title`
- `storyline`
- `platform` (ForeignKey → StreamPlatform)
- `active`
- `created`

### Review
Represents a user-submitted review.
- `review_user` (ForeignKey → User)
- `rating` (validated between 1 and 5)
- `watchlist` (ForeignKey → WatchList)
- `description`
- `created`
- `updated`
- `active`

---

## API Endpoints

### WatchLists

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/watch/list/` | Retrieve all watchlists |
| POST | `/watch/list/` | Create a watchlist |
| GET | `/watch/list/<id>/` | Retrieve a specific watchlist |
| PUT | `/watch/list/<id>/` | Update a watchlist |
| DELETE | `/watch/list/<id>/` | Delete a watchlist |

---

### Streaming Platforms

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/watch/platform/` | Retrieve all platforms |
| POST | `/watch/platform/` | Create a platform |
| GET | `/watch/platform/<id>/` | Retrieve a platform |
| PUT | `/watch/platform/<id>/` | Update a platform |
| DELETE | `/watch/platform/<id>/` | Delete a platform |

---

### Reviews

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/watch/list/<id>/create-review/` | Create a review |
| GET | `/watch/list/<id>/review/` | List reviews for a watchlist |
| GET | `/watch/list/review/<id>/` | Retrieve, update, or delete a review |

**Constraints**
- Each user may submit only one review per watchlist
- Ratings are restricted to values between 1 and 5

---

## Setup & Execution

### Clone the repository
```bash
git clone <repository-url>
cd watchmate
````

### Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create administrative user

```bash
python manage.py createsuperuser
```

### Run the server

```bash
python manage.py runserver
```

API base URL:

```
http://127.0.0.1:8000/watch/
```

---

## Engineering Principles Applied

* RESTful service design
* Object-Oriented Programming
* Relational data modeling
* Data validation and integrity enforcement
* HTTP protocol semantics
* Maintainable and extensible code structure

---

## Roadmap

* Token-based authentication (JWT)
* Pagination and filtering
* Rate limiting and throttling
* PostgreSQL production configuration
* Containerized deployment
* Observability and logging

---

## Author

Shubham Bhatt
Software Engineer – Backend (Python, Django)

```






