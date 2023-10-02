from django.urls import path
from rdapp import views
urlpatterns = [
    path('',views.home,name="home"),
    path('projects',views.projects,name="projects"),
    path('index',views.index,name="home"),
    path('skills',views.skills,name="skills"),
    path('education&exp',views.exp,name="education&exp"),
]
