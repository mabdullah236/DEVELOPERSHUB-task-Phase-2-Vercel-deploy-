```markdown
# Bookstore API - Phase 2 Task

## Live Demo
**Production URL:** [https://developershub-task-phase-2-production.up.railway.app/api/books/](https://developershub-task-phase-2-production.up.railway.app/api/books/)
*(Note: Use tools like Postman to interact with the API endpoints)*

## Project Overview
This project is a fully functional RESTful API built for a Bookstore. It allows users to perform CRUD (Create, Read, Update, Delete)
operations on a database of books. This was created as part of the **DEVELOPERSHUB Backend Development Internship (Phase 2)**.

### Advanced Features Implemented 
* **Search Functionality:** Search books by title.
* **Pagination:** Limits the number of books returned per page for optimized performance.
* **Data Validation:** Custom validation ensures `price` is positive and `isbn` is exactly 13 digits and numeric.
* **Authentication & Permissions:** Secure API endpoints. Only logged-in users can add books, and only the owner of a book can edit or delete it.
* **Production Ready:** Fully deployed with static file handling (WhiteNoise) and secure HTTP headers.

## Technologies Used
* **Backend Framework:** Django, Django REST Framework (DRF)
* **Language:** Python
* **Database:** SQLite (Local) / PostgreSQL (Production)
* **Deployment:** Railway.app
* **Tools:** Postman, Git & GitHub

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mabdullah236/DEVELOPERSHUB-task-Phase-2-.git](https://github.com/mabdullah236/DEVELOPERSHUB-task-Phase-2-.git)
   cd bookstore_api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   # source env/bin/activate # On macOS/Linux
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (For Authentication):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   *The server will start at `http://127.0.0.1:8000/`*

## API Endpoints

| Method | Endpoint | Description | Auth Required? |
|---|---|---|---|
| `GET` | `/api/books/` | Fetch all books (Supports Pagination) | No |
| `GET` | `/api/books/?search=<query>` | Search books by title | No |
| `POST` | `/api/books/` | Add a new book to the database | Yes (Logged In) |
| `GET` | `/api/books/<id>/` | Fetch one specific book by its ID | No |
| `PUT` | `/api/books/<id>/` | Update a specific book's details | Yes (Owner Only)|
| `DELETE` | `/api/books/<id>/` | Remove a book from the database | Yes (Owner Only)|

### Sample JSON Input (For POST and PUT requests)
*Note: Include Basic Authentication in your request headers for POST and PUT.*
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 1500,
  "isbn": "9780735211299",
  "published_date": "2018-10-16"
}
```