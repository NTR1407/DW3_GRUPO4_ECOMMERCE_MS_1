from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# Create your views here.

class VerifyTokenView(TokenVerifyView):

    def post(self, request, *args, **kwargs):
        token = request.data['token']
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            valid_data = tokenBackend.decode(token,verify=False)
            serializer.validated_data['UserId'] = valid_data['user_id']

        except TokenError as e:
            raise InvalidToken(e.args[0])
            
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

        # put y post llevan body
        # get y delet parametros por url
        # pip freezer > requirements.txt
class userInformation():

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # telephone = serializer.validated_data.get('telephone')
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            