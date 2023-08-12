from rest_framework import serializers

from apps.utils.validators import cellphone_validator
from .models import PhoneGroup, Phone


class InputPhoneCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=True, validators=[cellphone_validator])


class InputPhoneUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class OutputPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ("name", "phone")


class InputPhoneGroupCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class InputPhoneGroupAddMemberSerializer(serializers.Serializer):
    members = InputPhoneCreateSerializer(required=True, many=True)


class OutputPhoneGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneGroup
        fields = ("name", "members_count", "created_at", "updated_at")


class OutputPhoneGroupWithPhonesSerializer(serializers.ModelSerializer):
    members = OutputPhoneSerializer(many=True, read_only=True)

    class Meta:
        model = PhoneGroup
        fields = ("name", "members", "members_count", "created_at", "updated_at")
