from datetime import datetime

from apps.user.enums import PersonTypeEnum
from apps.user.models import User
from config.settings.documents import (
    DOCUMENTS_BUCKET,
    DOCUMENTS_UPLOAD_HOURS_EXPIRATION,
    PERSONAL_DOCUMENTS,
    LEGAL_DOCUMENTS,
)
from config.settings.storage import MINIO_CLIENT


def user_register(*, cellphone: str, first_name: str, last_name: str, email: str, person_type: bool) -> User:
    return User.objects.create_user(
        cellphone=cellphone,
        first_name=first_name,
        last_name=last_name,
        email=email,
        person_type=person_type,
    )


def user_update_last_login(*, user_id: int) -> None:
    User.objects.filter(id=user_id).update(last_login=datetime.now())


def user_generate_upload_document_url(*, document: str, user_id: int) -> str:
    user = User.objects.filter(id=user_id).first()
    if user.person_type == PersonTypeEnum.Real and document not in PERSONAL_DOCUMENTS:
        raise ValueError("incorrect document type")
    elif user.person_type == PersonTypeEnum.Legal and document not in LEGAL_DOCUMENTS:
        raise ValueError("incorrect document type")

    now = datetime.now()
    url = MINIO_CLIENT.presigned_put_object(
        bucket_name=DOCUMENTS_BUCKET,
        object_name=f"{now.year}/{now.month}/{now.day}/{user_id}/{document}.jpg",
        expires=DOCUMENTS_UPLOAD_HOURS_EXPIRATION,
    )

    return url
