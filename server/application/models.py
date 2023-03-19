import uuid
import datetime

from django.db import models
from django.urls import reverse_lazy

from authsystem.models import User

# Create your models here.

class ApplicationStatus(models.Model):
    title = models.CharField(max_length=128, unique=True)
    is_finaled = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Application status")
        verbose_name_plural = ("Application statusess")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("application_status_detail", kwargs={"pk": self.pk})

class ApplicationService(models.Model):
    title = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = ("Application service")
        verbose_name_plural = ("Application services")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("application_service_detail", kwargs={"pk": self.pk})

class ApplicationState(models.Model):
    title = models.CharField(max_length=128, unique=True)
    is_finaled = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Application status")
        verbose_name_plural = ("Application statusess")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("application_status_detail", kwargs={"pk": self.pk})

class Application(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    number = models.IntegerField()

    client = models.ForeignKey(User, on_delete=models.CASCADE)

    service = models.ForeignKey(ApplicationService, on_delete=models.PROTECT)
    current_status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT)
    state = models.ForeignKey(ApplicationState, on_delete=models.PROTECT, null=True, blank=True)
    
    entry_date = models.DateTimeField()
    finaled_date = models.DateTimeField(editable=True)

    @property
    def marked(self,):
        try:
            now = datetime.datetime.now()
            count_date = lambda now, taked: (now - taked).days
            result = count_date(now, self.finaled_date.replace(tzinfo=None))
            print(result)
            return result >= 5
        except:
            return True

    class Meta:
        verbose_name = ("Application")
        verbose_name_plural = ("Applications")

        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse_lazy("Application_detail", kwargs={"pk": self.pk})
