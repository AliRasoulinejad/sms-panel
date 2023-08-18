from django.urls import path, include


urlpatterns = [
    path("auth/", include(("apps.authentication.urls", "auth"))),
    path("phonebooks/", include(("apps.phonebook.urls", "phonebooks"))),
    path("senders/", include(("apps.senders.urls", "senders"))),
    path("users/", include(("apps.user.urls", "users"))),
]
