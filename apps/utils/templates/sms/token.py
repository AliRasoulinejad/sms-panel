from apps.utils.templates.sms.main import AbstractSMSTemplate


class TokenSMSTemplate(AbstractSMSTemplate):
    template = "کد ورود شما: [code]"
