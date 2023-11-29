from django.db import models


class BaseModel(models.Model):
    """
    Abstract model to be inherited by all models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
