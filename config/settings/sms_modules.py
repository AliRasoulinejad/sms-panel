from apps.utils.sms_modules import MagfaSMSModule
from config.env import env

sms_module_type = env.str('SMS_MODULE_TYPE', default='')

sms_module = {
    "MAGFA": MagfaSMSModule(
        base_url=env.str("MAGFA_BASE_URL", default=""),
        username=env.str("MAGFA_USERNAME", default=""),
        password=env.str("MAGFA_PASSWORD", default=""),
        domain=env.str("MAGFA_DOMAIN", default=""),
    )
}[sms_module_type]
