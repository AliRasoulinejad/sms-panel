import logging

from drf_spectacular.utils import extend_schema
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import InputUserRegisterSerializer, OutputUserSerializer
from apps.user.services.commands import user_register

logger = logging.getLogger(__name__)


class UserRegisterApi(APIView):
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


class UserSelfApi(APIView):
    @extend_schema(request=empty, responses=OutputUserSerializer, tags=["users"])
    def get(self, request):
        return Response(OutputUserSerializer(request.user, context={"request": request}).data)
