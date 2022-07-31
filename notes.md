# Concepts
- TemplateView
- ListView
- TestCase, SimpleTestCase


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
