from django.urls import path

from . import views

app_name = "submissions"

urlpatterns = [
    path("", views.home, name="home"),
    path("submit/", views.submit, name="submit"),
    path("submitted/", views.submitted, name="submitted"),
    path("status/", views.status_lookup, name="status_lookup"),
]

