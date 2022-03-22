from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    # path('user', views.UserView.as_view(), name='user'),
    # path('upload', views.UploadPictureView.as_view(), name='upload')
]