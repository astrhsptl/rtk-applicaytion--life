from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView,  RetrieveUpdateAPIView

from authsystem.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application, ApplicationService, ApplicationStatus, ApplicationState
from .serializers import ApplicationSerializer, ApplicationServiceSerializer, ApplicationStatusSerializer, ApplicationStateSerializer
from services.db_operations import application_get

class ApplicationStateListView(ListCreateAPIView):
    ''' API for Application Status db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationState.objects.all()
    serializer_class = ApplicationStateSerializer

class ApplicationStateRetrieveAPIView(RetrieveAPIView, RetrieveUpdateAPIView):
    ''' API for Application Status db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationState.objects.all()
    serializer_class = ApplicationStateSerializer

class ApplicationStatusListView(ListCreateAPIView):
    ''' API for Application Status db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

class ApplicationStatusRetrieveAPIView(RetrieveAPIView, RetrieveUpdateAPIView):
    ''' API for Application Status db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer


class ApplicationServiceListView(ListCreateAPIView):
    ''' API for Application Service db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationService.objects.all()
    serializer_class = ApplicationServiceSerializer

class ApplicationServiceRetrieveAPIView(RetrieveAPIView, RetrieveUpdateAPIView):
    ''' API for Application Service db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = ApplicationService.objects.all()
    serializer_class = ApplicationServiceSerializer

def r(**params):
    resp = lambda x : Response(ApplicationSerializer(x, many=True).data, status=status.HTTP_202_ACCEPTED)
    try:
        return resp(Application.objects.filter(**params))
    except:
        return Response({'detail': 'invalid itn'}, status=status.HTTP_400_BAD_REQUEST)

class ApplicationListView(ListCreateAPIView):
    ''' API for Application db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        return application_get(
                itn = request.GET.get('itn'),
                company_id = request.GET.get('company_id'),
                number = request.GET.get('number'),
                status_set = request.GET.get('finaled'),)

class ApplicationRetrieveAPIView(RetrieveAPIView, RetrieveUpdateAPIView):
    ''' API for Application db model. Support get, put, patch, delete. Queryset - concrete object '''
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

@api_view(['GET'])
def application_cheсk(request):
    number = request.GET.get('number')
    id = request.GET.get('id')

    resp = lambda x: Response(ApplicationSerializer(x).data, status=status.HTTP_200_OK)

    if number:
        try:
            return resp(filter(lambda m: m.marked, Application.objects.get(number=number)))
        except:
            return Response({})

    else: 
        if number:
            try:
                return resp(Application.objects.get(id=id))
            except:
                return Response({})
            
    return Response({})