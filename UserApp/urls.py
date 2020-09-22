from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^toUser/',views.toUser,name='toUser')
]