from django.urls import path, include
from rest_framework_simplejwt.views import token_refresh, token_verify

from apps.authentication.apis import JWTSendOTP, JWTVerifyOTP

urlpatterns = [
    path(
        "jwt/",
        include(
            (
                [
                    path("otp/", JWTSendOTP.as_view(), name="otp"),
                    path("otp/verify/", JWTVerifyOTP.as_view(), name="verify"),
                    path("refresh/", token_refresh, name="refresh"),
                    path("verify/", token_verify, name="verify"),
                ],
                "jwt",
            )
        ),
    ),
]
