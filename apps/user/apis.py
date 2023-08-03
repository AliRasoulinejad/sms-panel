import logging

from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import InputRegisterSerializer, OutputRegisterSerializer
from apps.user.services.commands import user_register

logger = logging.getLogger(__name__)


class UserRegisterApi(APIView):
    @extend_schema(request=InputRegisterSerializer, responses=OutputRegisterSerializer, tags=["users"])
    def post(self, request):
        serializer = InputRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = user_register(
            cellphone=data["cellphone"], first_name=data["first_name"], last_name=data["last_name"],
            email=data["email"], person_type=data["person_type"],
        )

        return Response(OutputRegisterSerializer(user, context={"request": request}).data)
