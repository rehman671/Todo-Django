# Todo Backend API
Todo App API
This is a Django Rest Framework API for managing Todo items.

## Getting Started
### Prerequisites
Python (version 3.6 or higher)
Django (version 3.0 or higher)
Django Rest Framework (version 3.12 or higher)



#### Installation

##### 1. Clone the repository:
        git clone https://github.com/rehman671/Todo.git


##### 2. Navigate to the project directory:
        cd Todo


##### 3. Create a virtual environment (optional):
        python3 -m venv venv


##### 4. Activate the virtual environment:
On macOS and Linux:

    source venv/bin/activate
On Windows:

    venv\Scripts\activate
##### 5. Apply the database migrations:
    python manage.py migrate

##### 6. Start the development server:
    python manage.py runserver



##### 7. Access the API at http://localhost:8000/api/v1/

#### API Endpoints
 #####  User Endpoints:

        GET /api/v1/user/: Retrieve all users.
        POST /api/v1/user/signup/: Register a new user.
        
        
#####  Task Endpoints:
   
    GET /api/v1/user/(user_id)/task: Retrieve all task of specific user.
    GET /api/v1/task/: Retrieve all tasks.
    POST /api/v1/task/: Create a new task.
    DELETE  /api/v1/task/ Delete a new task
    
    
#####  Authentication Endpoints:

    POST /api/v1/login/: User login.
    POST /api/v1/logout/: User logout.
    POST /api/v1/refresh/: Refresh access token 
    
    
    
Note: JWT Token Authentication has been implemented for login, and the token will be blacklisted on logout.
