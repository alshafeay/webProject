from django.urls import path , include
from blog import views

urlpatterns = [
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact"),
    path('services/', views.services , name="services"),
    path('shop/', views.shop , name="shop"),
    path('blog/', views.blog , name="blog"),
    path('', views.home , name="home"),
]

