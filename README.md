# Django-Ecommerce-Bookstore
<p>This is a RESTAPI should support CRUD operations on Ebook.API should also be able to return Ebook list that sorted and/or filtered ebooks by any of the fields.Uses token authentication to authenticate and to authorise the user.This RESTAPI supports multiple users.</p>

## Stack
- Python
- django
- SQLite
- vsc code


## Requirements
- Django 
- Pypi packages
- Database:SQLite
 

### API Actions:

* Create the book with title,author,genre,review,favourite

* Retrieve books details by the ID

* Update books and their fields

* Delete the added books

*retrieve a list of books associate with an author,genre,title


## EBook_App

Lets begin our project by starting our project and installing a books app, type below commands in terminal.

(django_project)$`django-admin startproject Ebook .` (do not avoid this period)

(django_project)$`python manage.py startapp bookapi`

Now, open your favourite IDE and locate this project directory. (Im using VS Code so it should be something like this) note that at this point django doesnt know about this app, therefore we need to mention this app name inside our settings.py file.

* settings.py 

open your Ebook folder, in here you will find settings.py file (open it). Go to Installed app section and mention your app name there (as shown below).


	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    # my apps,				# changes
	    'bookapi',
	    ]
      
      ### models

When done with the settings.py file, open the bookapi folder (our app), and create model Books with fields title,author,genre,review and favourite.

## migrations 

now its time to create some tables in our database, most of which is already handled by django, we just need to run following commands:

(django_project)$`python manage.py makemigrations`

(django_project)$`python manage.py migrate`

simply, the migrations command tells us what changes are going to be made in our database (right now two models will be created one is Book and other one is Order), the migrate command is just like conformation stage of makemigrations command (means if you agree with the changes mentioned by migrations command then in order to perform those changes we run migrate command) 

### server

Now, lets check that our model is being registered properly or not. First lets ensure that our server is running properly. Put the following commmand in terminal:

(django_project)$`python manage.py runserver`
 
 now open this link in your browser http://127.0.0.1:8000/
 
 ### views

 we need to work on views. In this case im gonna use 'Class Based ModelViews' which makes our code as much DRY (Don't Repeat Yourself) as possible and faster to implement and that does not provide any method handlers such as .get() or .post() , and instead provides actions such as .list() and .create() .

* The 'BookView' is a class which basically using the django module ListView to output the contents of Our book model and it performs the CRUD operations.

### urls

*The django. urls module within the Django project code base. path is used for routing URLs to the appropriate view functions within a Django application using the URL dispatcher.A request in Django first comes to urls.py and then goes to the matching function in views.py.



