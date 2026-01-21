from django.urls import path

from . import views

app_name = "submissions"

urlpatterns = [
    path("", views.home, name="home"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("submit/", views.submit, name="submit"),
    path("submitted/", views.submitted, name="submitted"),
    path("status/", views.status_lookup, name="status_lookup"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("terms/", views.terms_of_service, name="terms"),
    path("security/", views.security_transparency, name="security"),
]

