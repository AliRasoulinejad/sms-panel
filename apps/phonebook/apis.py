import logging

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import GenericViewSet

from apps.phonebook.models import PhoneGroup, Phone
from apps.phonebook.serializers import (
    InputPhoneCreateSerializer,
    OutputPhoneSerializer,
    InputPhoneUpdateSerializer,
    InputPhoneGroupCreateSerializer,
    OutputPhoneGroupSerializer,
    OutputPhoneGroupWithPhonesSerializer,
    InputPhoneGroupAddMemberSerializer,
)
from apps.phonebook.services.commands import (
    create_phone,
    update_phone,
    delete_phone,
    create_phone_group,
    update_phone_group,
    delete_phone_group,
    add_members_to_phone_group,
)
from apps.phonebook.services.queries import list_phone_group, list_phone, get_phone, get_phone_group

logger = logging.getLogger(__name__)


class PhoneCRUDApi(GenericViewSet):
    model = Phone
    queryset = model.objects.all()

    @extend_schema(request=InputPhoneCreateSerializer, responses=OutputPhoneSerializer, tags=["phonebook"])
    def create(self, request, *args, **kwargs):
        serializer = InputPhoneGroupCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_group = create_phone(owner_id=request.user.id, name=data["name"], phone=data["phone"])
        return Response(OutputPhoneGroupSerializer(phone_group, context={"request": request}).data)

    @extend_schema(request=InputPhoneUpdateSerializer, responses=OutputPhoneSerializer, tags=["phonebook"])
    def update(self, request, pk, *args, **kwargs):
        serializer = InputPhoneGroupCreateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        update_phone(instance_id=pk, owner_id=request.user.id, name=data["name"])
        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(responses=OutputPhoneGroupSerializer(many=True), tags=["phonebook"])
    def list(self, request, *args, **kwargs):
        queryset = list_phone(owner_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OutputPhoneGroupSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OutputPhoneGroupSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=OutputPhoneSerializer, tags=["phonebook"])
    def retrieve(self, request, *args, **kwargs):
        instance = get_phone(instance_id=int(kwargs["pk"]), owner_id=request.user.id)
        serializer = OutputPhoneSerializer(instance)
        return Response(serializer.data)

    @extend_schema(tags=["phonebook"])
    def destroy(self, request, *args, **kwargs):
        delete_phone(instance_id=int(kwargs["pk"]), owner_id=request.user.id)
        return Response(status=HTTP_204_NO_CONTENT)


class PhoneGroupCRUDApi(GenericViewSet):
    model = PhoneGroup
    queryset = model.objects.all()

    @extend_schema(request=InputPhoneGroupCreateSerializer, responses=OutputPhoneGroupSerializer, tags=["phonebook"])
    def create(self, request, *args, **kwargs):
        serializer = InputPhoneGroupCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_group = create_phone_group(owner_id=request.user.id, name=data["name"])
        return Response(OutputPhoneGroupSerializer(phone_group, context={"request": request}).data)

    @extend_schema(request=InputPhoneGroupCreateSerializer, responses=OutputPhoneGroupSerializer, tags=["phonebook"])
    def update(self, request, pk, *args, **kwargs):
        serializer = InputPhoneGroupCreateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        update_phone_group(instance_id=pk, owner_id=request.user.id, name=data["name"])
        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(responses=OutputPhoneGroupSerializer(many=True), tags=["phonebook"])
    def list(self, request, *args, **kwargs):
        queryset = list_phone_group(owner_id=request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OutputPhoneGroupSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OutputPhoneGroupSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=OutputPhoneGroupWithPhonesSerializer, tags=["phonebook"])
    def retrieve(self, request, *args, **kwargs):
        instance = get_phone_group(instance_id=int(kwargs["pk"]), owner_id=request.user.id)
        serializer = OutputPhoneGroupWithPhonesSerializer(instance)
        return Response(serializer.data)

    @extend_schema(tags=["phonebook"])
    def destroy(self, request, *args, **kwargs):
        delete_phone_group(instance_id=int(kwargs["pk"]), owner_id=request.user.id)
        return Response(status=HTTP_204_NO_CONTENT)

    @extend_schema(request=InputPhoneGroupAddMemberSerializer, tags=["phonebook"])
    @action(methods=["POST"], detail=True, url_path="add-members")
    def add_members(self, request, *args, **kwargs):
        serializer = InputPhoneGroupAddMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        add_members_to_phone_group(instance_id=int(kwargs["pk"]), owner_id=request.user.id, members=data["members"])
        return Response(status=HTTP_204_NO_CONTENT)
