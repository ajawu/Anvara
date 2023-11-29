from rest_framework.viewsets import ModelViewSet

from anvara_assessment.record.api.permissions import IsOwner
from anvara_assessment.record.api.serializers import RecordSerializer
from anvara_assessment.record.models import Record


class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsOwner]
    lookup_field = "pk"
    queryset = Record.objects.all()

    def get_queryset(self):
        return Record.objects.filter(created_by=self.request.user)
