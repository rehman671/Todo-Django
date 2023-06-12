# Todo backend Api
# Todo App API

This is a Django Rest Framework API for managing Todo items.

## Getting Started

### Prerequisites

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)
- Django Rest Framework (version 3.12 or higher)

### Installation

1. Clone the repository:

git clone https://github.com/rehman671/Todo.git


2. Navigate to the project directory:
cd Todo




3. Create a virtual environment (Optional):
python3 -m venv venv


4. Activate the virtual environment:
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

5. Install the dependencies:


6. Apply the database migrations:
python manage.py migrate



7. Start the development server:


python manage.py runserver





8. Access the API at `http://localhost:8000/api/v1/`

## API Endpoints

- User Endpoint:
- `GET /api/v1/user/`: Retrieve all users.
- `POST /api/v1/user/signup/`: Register a new user.

- Task Endpoint:
- `GET /api/v1/task/`: Retrieve all tasks.
- `POST /api/v1/task/`: Create a new task.

- Authentication Endpoints:
- `POST /api/v1/login/`: User login.
- `POST /api/v1/logout/`: User logout.

## Authentication and Permissions

This API uses token-based authentication. To access the protected endpoints (user and task endpoints), include the token in the request headers:





