"""
Next, we want to “include” both the accounts app and the built-in auth app.
The reason is that the built-in auth app already provides views and urls for log in and log out.
But for sign up we will need to create our own view and url.
To ensure that our URL routes are consistent we place them both at accounts/ so the eventual URLS will be /accounts/login, /accounts/logout, and /accounts/signup.


"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
