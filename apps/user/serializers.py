from rest_framework import serializers

from apps.utils.validators import cellphone_validator
from .enums import PersonTypeEnum, AuthorizeRequestEnum
from .models import User, AuthorizeRequest


class InputUserRegisterSerializer(serializers.Serializer):
    cellphone = serializers.CharField(required=True, validators=[cellphone_validator])
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=False)
    agreement = serializers.BooleanField(required=True)
    person_type = serializers.ChoiceField(choices=PersonTypeEnum.choices, default=PersonTypeEnum.Real)

    def validate_cellphone(self, cellphone):
        if User.objects.filter(cellphone__exact=cellphone).exists():
            raise serializers.ValidationError("cellphone already exist")
        return cellphone

    def validate_agreement(self, agreement):
        if not agreement:
            raise serializers.ValidationError("agreement is required")
        return agreement


class OutputUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("cellphone", "first_name", "last_name", "email", "person_type")


class InputUserDocumentSerializer(serializers.Serializer):
    document = serializers.CharField(required=True)


class OutputUserDocumentSerializer(serializers.Serializer):
    url = serializers.URLField()


class InputAuthorizeRequestSerializer(serializers.Serializer):
    request_type = serializers.ChoiceField(required=True, choices=AuthorizeRequestEnum.choices)
    data = serializers.JSONField(required=True)

    def validate_data(self, data):
        return data


class OutputAuthorizeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizeRequest
        fields = ("request_type", "data", "status")
