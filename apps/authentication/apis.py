import logging

from drf_spectacular.utils import extend_schema
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import User
from apps.user.services.commands import user_update_last_login
from .serializers import InputSendOTPSerializer, InputVerifyOTPSerializer, OutputVerifyOTPSerializer
from .services.commands import authentication_send_otp, authentication_verify_otp

logger = logging.getLogger(__name__)


class JWTSendOTP(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(request=InputSendOTPSerializer, responses=empty, tags=["authentication"])
    def post(self, request):
        serializer = InputSendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        authentication_send_otp(cellphone=data["cellphone"])

        return Response(status=HTTP_204_NO_CONTENT)


class JWTVerifyOTP(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(request=InputVerifyOTPSerializer, responses=OutputVerifyOTPSerializer, tags=["authentication"])
    def post(self, request):
        serializer = InputVerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        code_is_valid = authentication_verify_otp(cellphone=data["cellphone"], code=data["code"])
        if not code_is_valid:
            return Response(status=HTTP_400_BAD_REQUEST)

        user = User.objects.get(cellphone=data["cellphone"])
        refresh = TokenObtainPairSerializer.get_token(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        result = OutputVerifyOTPSerializer(data=data, context={"request": request})
        result.is_valid(raise_exception=True)
        user_update_last_login(user_id=user.id)

        return Response(data=result.data)
