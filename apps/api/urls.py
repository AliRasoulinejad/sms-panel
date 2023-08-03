from django.urls import path, include


urlpatterns = [
    path("auth/", include(("apps.authentication.urls", "auth"))),
    path("user/", include(("apps.user.urls", "user"))),
]
