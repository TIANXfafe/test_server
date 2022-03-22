from rest_framework import views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from .authorizations import generate_jwt
from .serializers import UserSerializer

# Create your views here.
User = get_user_model()


class LoginView(views.APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = now()
            user.save()
            token = generate_jwt(user)
            user_serializer = UserSerializer(user)
            return Response(data={"token": token, "user": user_serializer.data})
        else:
            print(serializer.error)
            return Response(data={"message": "数据提交错误！"})
