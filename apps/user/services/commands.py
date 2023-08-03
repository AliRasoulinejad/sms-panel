from apps.user.models import User


def user_register(*, cellphone: str, first_name: str, last_name: str, email: str, person_type: bool) -> User:
    return User.objects.create_user(
        cellphone=cellphone, first_name=first_name, last_name=last_name, email=email, person_type=person_type,
    )
