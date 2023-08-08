from rest_framework_simplejwt.authentication import JWTAuthentication as BaseJWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from rest_framework_simplejwt.settings import api_settings

from apps.user.models import User


class JWTAuthentication(BaseJWTAuthentication):
    www_authenticate_realm = "api"
    media_type = "application/json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = User

    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError as e:
            raise InvalidToken(
                "Token contained no recognizable user identification"
            ) from e

        try:
            user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except self.user_model.DoesNotExist as e:
            raise AuthenticationFailed("User not found", code="user_not_found") from e

        return user
