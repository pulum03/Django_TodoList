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
from django.conf.urls import url
#from django.conf.urls import include
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'todo_board'


urlpatterns = [
    url(r'^$', views.Todo_board.as_view(), name = 'todo_board'),
    url(r'^insert/$', views.check_post, name = 'todo_board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Todo_board_detail.as_view(), name = 'todo_board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Todo_board_update.as_view(), name = 'todo_board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Todo_board_delete.as_view(), name = 'todo_board_delete'),

    url(r'^is_complete/$', views.check_post, name='todo_board_is_complete'),
    url(r'^is_non_complete/$', views.check_post, name='todo_board_is_non_complete'),
    
    url(r'^save_prioirity/$', views.check_post, name='todo_board_save_priority'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)