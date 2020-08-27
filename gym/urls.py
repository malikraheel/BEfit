from django.urls import path
from django.views.generic.base import RedirectView
from .import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('feature/', views.feature, name='feature'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bmi/', views.bmi, name='bmi'),
    path('price/', views.price, name='price'),
    path('videos/', views.videos, name='videos'),
    path('videos/<str:id>', views.videos),
    path('schedule/', views.schedule, name='schedule'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view()),
    path('profile/edit/<int:pk>',
         views.ProfileUpdateView.as_view(success_url="/gym/home")),
    path("message/", views.MessageCreate.as_view(success_url='/gym/home'), name='message'),
    path('', RedirectView.as_view(url='home/')),
]
