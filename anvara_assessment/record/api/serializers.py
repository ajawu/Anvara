from datetime import datetime

from rest_framework import serializers

from anvara_assessment.record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        exclude = ["created_by"]

    def validate_date_of_birth(self, value):
        if value >= datetime.today().date():
            raise serializers.ValidationError("Date of birth has to be in the past")
        return value

    def validate_date_of_treatment(self, value):
        if value <= datetime.today().date():
            raise serializers.ValidationError("Date of treatment has to be in the future")
        return value

    def save(self, **kwargs):
        self.validated_data["created_by"] = self.context["request"].user
        return super().save(**kwargs)
