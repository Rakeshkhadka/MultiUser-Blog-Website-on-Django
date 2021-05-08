from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from base.views import home, posts, robots_txt, article, unpublishedposts, CreateForm, UpdateForm, DeleteForm, RegisterPage, LoginPage, LogoutUser, UnpublishedUpdateForm, User_ChangePassword
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.article, name='article'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('change_password/', views.User_ChangePassword, name='change_password'),
    path('create-post/', views.CreateForm, name = 'create-post'),
    path('update-post/<slug:slug>/', views.UpdateForm, name = 'update-post'),
    path('unpublishedposts/', views.unpublishedposts, name='unpublishedposts'),
    path('unpublished-update-post/<slug:slug>/', views.UnpublishedUpdateForm, name = 'unpublished-update-post'),

    path('delete-post/<slug:slug>/', views.DeleteForm, name = 'delete-post'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='base/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_done.html'), name="password_reset_complete"),
    path('robots.txt/', views.robots_txt, name="robots.txt"),
]