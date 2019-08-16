Django sample web application. 

Handles resume/application submission from all users. Ordinary users enter their name, mail id and upload their resume to the server.
Admin users can view submitted applications and edit and change resume status from 'Applied' to 'Viewed','Accepted' or 'Rejected'.

Python/Django versions: Python 3.7 and Django 2.2.4

Backend connected: sqlite

Application has been developed using Django framework

Django features involved:

1. Forms
2. Models
3. Views
4. Routes
5. Templating
6. Admin

Setup:

1. Clone the repo
2. Setup virtual environment(ex: virtualenv -p python3 env)
3. pip install -r requirements.txt (pip with latest version based on python3)
4. python3 manage.py migrate
5. python3 manage.py createsuperuser (to create admin user credentials in local)
6. python3 manage.py runserver

Hit the browser with,
1. http://127.0.0.1:8000/admin  
   This link shows login for admin users. Use the credentials used in 5th step of setup above to login as admin.
2. http://127.0.0.1:8000/resumesender/
   This link will open up the index page. Index page will have 2 links.
      Link1: Show Resumes: http://127.0.0.1:8000/resumesender/show . 
	  This 'show' link will open only for admins who logged in to the admin page using admin link. 'show' page lists all resumes uploaded. 
	  It also provides CRUD operations on resume documents.
	  Admin user can modify the resume_status of a document and change resume status from 'Applied' to 'Viewed','Accepted' or 'Rejected'.
      	  
      Link2:  Upload new resume: http://127.0.0.1:8000/resumesender/profile/
      Any candidate user can access this 'upload' url and upload his/her resume along with name, mail id and date.

17 Aug 2019


