from django.urls import path
from . import views


urlpatterns = [
	path("get_and_post", views.get_and_post),
	path("redirected/", views.redirected, name="redirected"),
	path("users/", views.all_users, name="users"),
	path("users/add/", views.add_user, name="add"),
	path("users/update/<int:pk>/", views.update_user),
	path("users/delete/<int:pk>/", views.delete_user),
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
]