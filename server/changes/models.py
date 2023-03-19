import uuid
from django.db import models
from django.urls import reverse_lazy

from authsystem.models import User
from application.models import Application, ApplicationStatus, ApplicationState


class Change(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    
    manager = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    application = models.ForeignKey(Application, on_delete=models.PROTECT)

    former_status = models.ForeignKey(ApplicationStatus, related_name="former_status", on_delete=models.PROTECT, null=True, blank=True)
    current_status = models.ForeignKey(ApplicationStatus, related_name="current_status", on_delete=models.PROTECT)
    current_state = models.ForeignKey(ApplicationState, on_delete=models.PROTECT, null=True, blank=True)
    
    create_entry = models.DateTimeField(auto_now_add=True, editable=False)
    create_date = models.DateTimeField(editable=True,
        blank=True, null=True,                                   
    )

    class Meta:
        verbose_name = ("Change")
        verbose_name_plural = ("Changes")

    def __str__(self):
        return "change"

    def get_absolute_url(self):
        return reverse_lazy("change_detail", kwargs={"pk": self.pk})