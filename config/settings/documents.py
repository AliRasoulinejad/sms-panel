from datetime import timedelta

from config.env import env

DOCUMENTS_BUCKET = env.str("DOCUMENTS_BUCKET", "documents")
DOCUMENTS_UPLOAD_HOURS_EXPIRATION = timedelta(hours=env.int("DOCUMENTS_UPLOAD_HOURS_EXPIRATION", 6))

PERSONAL_DOCUMENTS = env.list("PERSONAL_DOCUMENTS", default=[])
LEGAL_DOCUMENTS = env.list("LEGAL_DOCUMENTS", default=[])
