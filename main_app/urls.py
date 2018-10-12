from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('skills/', views.skills_index, name='skills_index'),
    path('skills/<int:skill_id>', views.skills_detail, name='skills_detail'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),

]
