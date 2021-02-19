from django.urls import path
from . import views

urlpatterns = [
    path("", views.root),
    path("handle_data", views.handle_data),
    # path("too_low", views.too_low),
    # path("too_high", views.too_high),
    # path("success", views.success),
    path("reset", views.reset)
]