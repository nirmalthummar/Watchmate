from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {
                'message': "The registration done successfully!",
                'username': account.username,
                'email': account.email
            }
            # token = Token.objects.get(user=account)
            # data['token'] = token.key

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)


@api_view(['POST'])
def logout(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(
            {
                "message": "You have successfully logout!"
            },
            status=status.HTTP_200_OK
        )
