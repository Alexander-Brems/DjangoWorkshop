"""myapp5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *

urlpatterns = [

    # Add View
    path('add', NoteCreate.as_view(), name='note-add'),

    # Edit View
    path('<int:pk>/', NoteUpdate.as_view(), name='note-update'),

    # Delete View
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),

    # List View
    path('', NoteList.as_view(), name='note-list'),
]
