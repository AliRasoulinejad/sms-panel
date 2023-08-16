import logging

from drf_spectacular.utils import extend_schema
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import (
    InputUserRegisterSerializer,
    OutputUserSerializer,
    InputUserDocumentSerializer,
    OutputUserDocumentSerializer,
    InputAuthorizeRequestSerializer,
    OutputAuthorizeRequestSerializer,
)
from apps.user.services.commands import user_register, user_generate_upload_document_url, user_request_to_authorize

logger = logging.getLogger(__name__)


class UserRegisterAPI(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(request=InputUserRegisterSerializer, responses=OutputUserSerializer, tags=["users"])
    def post(self, request):
        serializer = InputUserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = user_register(
            cellphone=data["cellphone"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            person_type=data["person_type"],
        )

        return Response(OutputUserSerializer(user, context={"request": request}).data)


class UserSelfAPI(APIView):
    @extend_schema(request=empty, responses=OutputUserSerializer, tags=["users"])
    def get(self, request):
        return Response(OutputUserSerializer(request.user, context={"request": request}).data)


class UserUploadDocumentAPI(APIView):
    @extend_schema(request=InputUserDocumentSerializer, responses=OutputUserDocumentSerializer, tags=["users"])
    def post(self, request):
        serializer = InputUserDocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        url = user_generate_upload_document_url(document=data["document"], user_id=request.user.id)
        out = OutputUserDocumentSerializer(data={"url": url}, context={"request": request})
        out.is_valid()

        return Response(out.data)


class UserAuthorizeAPI(APIView):
    @extend_schema(request=InputAuthorizeRequestSerializer, responses=OutputAuthorizeRequestSerializer, tags=["users"])
    def post(self, request):
        serializer = InputAuthorizeRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        authorize_request = user_request_to_authorize(
            user_id=request.user.id,
            request_type=data["request_type"],
            data=data["data"],
        )

        return Response(OutputAuthorizeRequestSerializer(authorize_request, context={"request": request}).data)
