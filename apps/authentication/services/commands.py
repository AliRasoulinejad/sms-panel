from django.core.cache import cache

from apps.user.models import User
from apps.utils.templates.sms import TokenSMSTemplate
from apps.utils.token_generator import token_generator
from config.env import env


def authentication_send_otp(*, cellphone: str):
    u = User.objects.get(cellphone=cellphone)
    token = token_generator()
    token_ttl = env.int("LOGIN_TOKEN_TTL", default=2)
    cache.set(f"token:{cellphone}", str(token), timeout=token_ttl * 60)
    TokenSMSTemplate.send(user_id=u.id, cellphone=u.cellphone, code=token)

def authentication_verify_otp(*, cellphone: str, code: str) -> bool:
    token = cache.get(f"token:{cellphone}")

    return token==code
