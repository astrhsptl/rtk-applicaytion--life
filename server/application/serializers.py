from rest_framework import serializers

from .models import Application, ApplicationService, ApplicationStatus, ApplicationState


class ApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application
        fields = ("__all__")


class ApplicationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationService
        fields = ("__all__")


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ("__all__")


class ApplicationStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationState
        fields = ("__all__")
