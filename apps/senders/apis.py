import logging

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import GenericViewSet

from .models import Sender
from .serializers import InputSenderCreateSerializer, OutputSenderSerializer
from .services.commands import create_sender, delete_sender, upgrade_sender
from .services.queries import list_senders, get_sender

logger = logging.getLogger(__name__)


class SenderCRUDApi(GenericViewSet):
    model = Sender
    queryset = model.objects.all()

    @extend_schema(request=InputSenderCreateSerializer, responses=OutputSenderSerializer, tags=["senders"])
    def create(self, request, *args, **kwargs):
        serializer = InputSenderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        create_sender(user_id=request.user.id, number=data["number"])

        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(responses=OutputSenderSerializer(many=True), tags=["senders"])
    def list(self, request, *args, **kwargs):
        queryset = list_senders(owner_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OutputSenderSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OutputSenderSerializer(queryset, many=True)

        return Response(serializer.data)

    @extend_schema(responses=OutputSenderSerializer, tags=["senders"])
    def retrieve(self, request, *args, **kwargs):
        instance = get_sender(instance_id=int(kwargs["pk"]), owner_id=request.user.id)
        serializer = OutputSenderSerializer(instance)

        return Response(serializer.data)

    @extend_schema(tags=["senders"])
    def destroy(self, request, *args, **kwargs):
        delete_sender(instance_id=int(kwargs["pk"]), owner_id=request.user.id)

        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(tags=["senders"])
    @action(methods=["POST"], detail=True, url_path="upgrade")
    def upgrade(self, request, *args, **kwargs):
        upgrade_sender(instance_id=int(kwargs["pk"]), user_id=request.user.id)

        return Response(status=HTTP_204_NO_CONTENT)
