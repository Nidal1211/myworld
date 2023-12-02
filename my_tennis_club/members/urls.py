from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
      path('members/login/', views.login, name='signin'),
    path('signup/', views.register, name='signup'),
    path('einloggen/', views.login_member, name='einloggen'),
     
     
     ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)