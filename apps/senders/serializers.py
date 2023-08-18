from rest_framework import serializers

from .models import Sender


class InputSenderCreateSerializer(serializers.Serializer):
    number = serializers.CharField(required=True)


class OutputSenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender
        fields = (
            "number",
            "is_shared",
        )


class InputSenderUpgradeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
