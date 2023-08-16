from django.urls import path

from .apis import UserRegisterAPI, UserSelfAPI, UploadDocument

urlpatterns = [
    path("register", UserRegisterAPI.as_view(), name="register"),
    path("self", UserSelfAPI.as_view(), name="self"),
    path("documents", UploadDocument.as_view(), name="documents"),
]
