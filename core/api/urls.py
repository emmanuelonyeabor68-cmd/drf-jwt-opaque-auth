from django.urls import path
from .views import protected_view
from .views import LoginView, RefreshView, LogoutView

urlpatterns = [ 
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('protected/', protected_view),
]