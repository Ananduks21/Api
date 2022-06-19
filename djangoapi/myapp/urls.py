from django.urls import path
from . import views

urlpatterns=[
    path('',views.FuncList.as_view()),
    path('<int:pk>/',views.FuncDetail.as_view())
]