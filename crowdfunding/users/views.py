from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import CustomUser #'.models' means the models.py in the same branch
from .serializers import CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CustomUserList(APIView):
    def get(self, request): #getting a list of users
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request): #ability to create new users
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user) #we donot need many anymore, only unique instance is required
        return Response(serializer.data)
    
    def put(self, request, pk):
        print(f"updating: {pk}")
        pledge = self.get_object(pk) #giving the instance to the "serializers"-instance
        serializer = CustomUserSerializer(
            instance=CustomUser,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )   

class  CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs): #using args, kwargs
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request} #instruct behind the scenes
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] #ensuring users are valid data

        token, created = Token.objects.get_or_create(user=user) #function we are about to call return multiple items/spreading; get/create a token for a user

        # token, created can be replaced by any random text eg. token, _; token, happy

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        }) #next defining our URLs