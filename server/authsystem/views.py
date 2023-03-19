from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status

from services.authentication import authentication, register
from .serializers import (
    LoginSerializer, RegisterSerializer, 
    StartPasswordRestoreSerializer, UserStatusSerializer,
    UserPresentationSerializer,
)

from .models import User, UserStatus
from .serializers import UserPatchingSerializer, LoginRequestSerializer, LoginSerializer

class LoginAPIView(generics.GenericAPIView):
    '''This api relise sign in on jwt architecture. Return name, surname, email, is_superuser, is_staff and access token. Supports only post request'''
    serializer_class = LoginRequestSerializer
    
    def post(self, request) -> Response:
        response_description, response_status = authentication(request, LoginSerializer)
        return Response(response_description, status=response_status)

class RegisterAPIView(generics.GenericAPIView):
    '''This api relise sign up on jwt architecture. Return  name, surname, email, is_superuser, is_staff '''
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request) -> Response:
        response_description, response_status = register(request, self.serializer_class)
        return Response(response_description, status=response_status)

class UserInformationAndPatchingListView(generics.ListAPIView):
    ''' API for User db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = User.objects.all()
    serializer_class = UserPatchingSerializer

    def get(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username:
            return Response(self.serializer_class(User.objects.get(username=username)).data)
        return super().get(request, *args, **kwargs)

class UserInformationAndPatchingRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    ''' API for User db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = User.objects.all()
    serializer_class = UserPatchingSerializer

class UserStatusesListView(generics.ListCreateAPIView):
    ''' API for User db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

class UserStatusesRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    ''' API for User db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

@api_view(['GET'])
def company_cheсk(request):
    itn = request.GET.get('itn')
    id = request.GET.get('id')

    resp = lambda x: Response(UserPatchingSerializer(x).data, status=status.HTTP_200_OK)

    if itn:
        try:
            return resp(User.objects.get(itn=itn))
        except:
            return Response({})

    else: 
        if itn:
            try:
                return resp(User.objects.get(id=id))
            except:
                return Response({})
            
    return Response({})

@api_view(['GET'])
def itn_search(request):
    itn = request.GET.get('itn')
    if itn:
        return Response(UserPresentationSerializer(User.objects.filter(itn__contains=itn), many=True).data, status=status.HTTP_200_OK)
    
    return Response(UserPresentationSerializer(User.objects.all(), many=True).data, status=status.HTTP_200_OK)
