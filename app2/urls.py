from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('third/',third,name='third'),
    path('four/',four,name='four'),
]