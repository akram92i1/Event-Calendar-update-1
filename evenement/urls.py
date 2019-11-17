from django.urls import path 
from . import views

# 1- objective is to make my url dynamic 

urlpatterns = [
  path('in', views.index_page, name='index'),
  path('sd',views.Add_domain,name='add_domain'),
  path('nav!!bard',views.get_nav_bar,name='nav_nbar'),
  path('dfsdf',views.add_question_cours,name='add_question'),
  path('dfsd',views.Calendar_print,name='Calendar_print'),
  path('events_details/<int:app_label>/', views.Events_deatil,name='detail')
]
