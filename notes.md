# Concepts
- TemplateView, ListView, DetailView
- TestCase, SimpleTestCase
- models fields: CharField, TextField, ForeignKey


# Notes
- whenever we create or modify an existing model we’ll need to update Django in a two-step process
	1. First, we create a migrations file with the makemigrations command. Migration files create a reference of any changes to the database models which means we can track changes–and debug errors as necessary–over time.
	2. Second, we build the actual database with the migrate command which executes the instructions in our migrations file.
- If you simply run `python manage.py makemigrations` instead of `python manage.py makemigrations <app_name>`, a migrations file will be created for all available changes throughout the Django project. That is fine in a small project such as ours with only a single app, but most Django projects have more than one app! Therefore ,if you made model changes in multiple apps the resulting migrations file would include all those changes! This is not ideal. Migrations file should be as small and concise as possible as this makes it easier to debug in the future or even roll back changes as needed. Therefore, as a best practice, adopt the habit of always including the name of an app when executing the makemigrations command!
- To use Django Admin, first create superuser
	- `python manage.py createsuperuser`
	- register your app, in admin.py
- It’s important that all our test methods start with the phrase `test_` so that Django knows to test them! 
- [reverse()](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse) function. This basically returns the path, e.g. '/aboutpage', for the url name, that we set in the urls.py files. [Better Explanation](https://stackoverflow.com/questions/11241668/what-is-reverse). It takes an input of a url name and gives the actual url, which is reverse to having a url first and then give it a name.
- The *blog* app, shows how to use crud, and using static files
- ON DELETE CASCADE constraint is used to delete the rows from the child table automatically, when the rows from the parent table are deleted.
- You cannot edit the admin.py file before creating the superuser. If you edit the admin.py file and then try to create the superuser, you will get error
- some fields in django model cannot be left blank, if however you want to do that then use [this](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options)

### Setting up project level static file for your project. [Docs](https://docs.djangoproject.com/en/3.2/ref/settings/#static-files)
- CSS, JavaScript, and images are a core piece of any modern web application and within the Django world are referred to as “static files.”
- By default, Django will look within each app for a folder called `static`. In other words, a folder called `app_name/static/`. If you recall, this is si- Before each new deployment, the collectstatic command must be run to compilemilar to how templates are treated as well.
- As Django projects grow in complexity over time and have multiple apps, it is often simpler to reason about static files if they are stored in a single, project-level directory instead. 
- Steps
	1. create a new directory called *static* in the same folder as the *manage.py* file.
	2. Then we need to tell Django to look for this new folder when loading static files. Look at the bottom of the settings.py file, there is already a single line of configuration `STATIC_URL = '/static/'`
	3. By configuring `STATICFILES_DIRS` , we can tell Django where to look for static files beyond just `app/static` folder.
- `STATIC_ROOT`: is useless during development, it's only required for deployment. When your project goes live, things differ. Most likely you will serve dynamic content using Django and static files will be served by Nginx. Why? Because Nginx is incredibly efficient and will reduce the workload off Django.This is where STATIC_ROOT becomes handy, as Nginx doesn't know anything about your Django project and doesn't know where to find static files. So you set STATIC_ROOT = '/some/folder/' and tell Nginx to look for static files in /some/folder/. Then you run manage.py collectstatic and Django will copy static files from all the apps you have to /some/folder/.
- While in development, STATIC_ROOT does nothing. You don't even need to set it. Django looks for static files inside each app's directory (myProject/appName/static) and serves them automatically. This is the magic done by manage.py runserver when DEBUG=True.
- `STATICFILES_DIRS`: is used to include additional directories for collectstatic to look for. For example, by default, Django doesn't recognize /myProject/static/. So you can include it yourself.
- MEDIA_ROOT where media files ,all uploaded files goes. Example : Images, Files
- https://stackoverflow.com/questions/24022558/differences-between-staticfiles-dir-static-root-and-media-root
- Need more clarity on: STATIC_URL, STATIC_ROOT, MEDIA_ROOT, STATICFILES_DIRS, collectstatic, 
- collectstatic: collectstatic command which compiles all static files throughout the project into a singe directory suitable for deployment. 
- STATIC_ROOT: absolute location of these collected files, to a folder called staticfiles
- STATICFILES_STORAGE: file storage engine used by collectstatic
- Before each new deployment, the collectstatic command must be run to compile them into this staticfiles folder used in production.
- While there are multiple ways to serve these compiled static files in production, the most common approach–and the one we will use here–is to introduce the **WhiteNoise** package.
- **serving static files**: First, for local development, we created a top-level static folder and updated STATICFILES_DIRS to point to it. Then, we added configurations for STATIC_ROOT and STATICFILES_STORAGE before running collectstatic for the first time, which compiled all our static files across the entire project into a single *staticfiles* folder. Finally, we installed whitenoise, updated INSTALLED_APPS, MIDDLEWARE, and STATICFILES_STORAGE, and re-ran collectstatic.

# Authentication
- Whenever you create a new project, by default Django installs the auth app, which provides us with a User object107 containing: username, password, email, first_name, last_name. We use this `User` object to implement log in, log out, and sign up in our blog application
- by default Django will look within templates for a directory called *registration* for a file called login.html for a log in form.
- the *accounts* app in blog project is dedicated to create a signup form. You dont need this if you just need login/logout
- The order of our urls matters here because Django reads this file top-to-bottom. 
