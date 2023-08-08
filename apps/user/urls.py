from django.urls import path

from .apis import UserRegisterApi, UserSelfApi

urlpatterns = [
    path("register", UserRegisterApi.as_view(), name="register"),
    path("self", UserSelfApi.as_view(), name="self"),
]
