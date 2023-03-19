from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Change
from application.models import Application, ApplicationStatus
from authsystem.models import User
from .serializers import ChangeSerializer, ChangeGetSerializer
from services.db_operations import make_chage

class AddChange(ListCreateAPIView):
    queryset = Change.objects.all()
    serializer_class = ChangeSerializer

    def get(self, request, *args, **kwargs):
        manager = request.query_params.get('manager')
        application = request.query_params.get('application')

        resp = lambda x: Response(ChangeGetSerializer(x, many=True).data, status=status.HTTP_200_OK)

        if application:
            return resp(Change.objects.filter(application=application).order_by('-create_date'))
        elif manager:
            return resp(Change.objects.filter(manager=manager).order_by('-create_date'))
        return Response({"detail": "use query params manager or application"}, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        return make_chage(request)