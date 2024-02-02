from django.db import models


class VisaType(models.Model):
    # Visa Information
    visa_name = models.CharField(max_length=100)
    visa_description = models.TextField()
    application_requirements = models.TextField()
    processing_time = models.CharField(max_length=50)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.visa_name
