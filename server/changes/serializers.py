from rest_framework import serializers

from .models import Change
from application.serializers import ApplicationSerializer

class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = ("application", "current_status", "create_entry", "create_date", "current_state", "manager")

class ChangeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = ("__all__")
