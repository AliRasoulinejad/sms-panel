from django.urls import path

from .apis import (
    UserRegisterAPI,
    UserSelfAPI,
    UserUploadDocumentAPI,
    UserAuthorizeAPI,
)

urlpatterns = [
    path("register", UserRegisterAPI.as_view(), name="register"),
    path("self", UserSelfAPI.as_view(), name="self"),
    path("documents", UserUploadDocumentAPI.as_view(), name="documents"),
    path("authorize", UserAuthorizeAPI.as_view(), name="authorize"),
]
