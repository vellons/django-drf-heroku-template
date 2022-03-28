from django.urls import path

from users import views

urlpatterns = [
    path('', views.ProfileCreateAPIView.as_view()),
    path('<int:pk>/', views.ProfileRetrieveAPIView.as_view())
]
