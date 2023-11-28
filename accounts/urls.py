from django.urls import path
from shop import views
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup')
]
