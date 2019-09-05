"""todoSubject URL Configuration

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
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_main.urls')), # localhost:8000/으로 들오면 todo_main.urls로 연동
    path('index/', include('todo_main.urls')), # localhost:8000/index로 들오면 todo_main.urls로 연동 
    path('home/', include('todo_main.urls')),
    
    # board app
    path('board/', include('todo_board.urls')),
]
