from django.core.validators import RegexValidator
from django.utils.regex_helper import _lazy_re_compile

cellphone_validator = RegexValidator(
    _lazy_re_compile(r"^\+989\d{9}$"),
    message="Enter a valid cellphone",
    code="invalid",
)
