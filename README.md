# AccuKnox
# API for social networking application using Django Rest Framework

This project implements a simple API for social networking application using Django Rest Framework.


## Prerequisites

- Python (3.x recommended)
- Django
- Django REST Framework

## Installation

1. Clone the repository:

   git clone https://github.com/Meet-RT/AccuKnox_Practical_Task.git
   cd AccuKnox_Practical_Task

Create a virtual environment (optional but recommended):
python -m venv venv
Activate the virtual environment:


On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Apply database migrations:
python manage.py migrate


Create a superuser (for accessing the Django admin):
python manage.py createsuperuser
Follow the prompts to create a superuser account.

Usage
Run the development server:
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.


Access the Django admin interface:
Navigate to http://127.0.0.1:8000/admin/
Log in with the superuser credentials created earlier.
Create a few users and start sending, accepting, and rejecting friend requests using the API endpoints:



/api/register/ (POST): User register
/api/login/ (POST): User Login
/api/users/?keyword=meet@gmail.com (GET): Search User
/api/friend-requests/ (POST): Send a friend request.
/api/friend-requests/5/accept_friend_request/ (PATCH): Accept a friend request.
/api/friend-requests/5/reject_friend_request/ (PATCH): Reject a friend request.
/api/friend-requests/friends/ (GET): List of friends.
/api/friend-requests/pending_requests/ (GET): List of pending friend requests.
