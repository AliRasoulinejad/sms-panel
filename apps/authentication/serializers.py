from rest_framework import serializers

from apps.user.models import User, cellphone_validator


class InputSendOTPSerializer(serializers.Serializer):
    cellphone = serializers.CharField(required=True, validators=[cellphone_validator])

    def validate_cellphone(self, cellphone):
        if not User.objects.filter(cellphone__exact=cellphone).exists():
            raise serializers.ValidationError("cellphone already exist")
        return cellphone

class InputVerifyOTPSerializer(serializers.Serializer):
    cellphone = serializers.CharField(required=True, validators=[cellphone_validator])
    code = serializers.CharField(required=True, allow_blank=False)


class OutputVerifyOTPSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
