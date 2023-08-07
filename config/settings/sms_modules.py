from apps.utils.sms_modules import MagfaSMSModule
from config.env import env

sms_module_type = env('SMS_MODULE_TYPE', default='')

sms_module = {
    "MAGFA": MagfaSMSModule(
        base_url=env("MAGFA_BASE_URL", default=""),
        username=env("MAGFA_USERNAME", default=""),
        password=env("MAGFA_PASSWORD", default=""),
        domain=env("MAGFA_DOMAIN", default=""),
    )
}[sms_module_type]
