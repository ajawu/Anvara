from django.contrib.auth import get_user_model
from django.db import models

from anvara_assessment.utils.models import BaseModel

User = get_user_model()


class Record(BaseModel):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    date_of_treatment = models.DateField()
    doctor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="patient_records")
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="medical_records")

    def __str__(self):
        return f"{self.name} - {self.date_of_treatment}"
