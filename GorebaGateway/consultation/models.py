from django.db import models


class Consultant(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    # Professional Information
    job_title = models.CharField(max_length=50)

    # Availability
    available_days = models.CharField(max_length=50)
    available_hours_start = models.TimeField()
    available_hours_end = models.TimeField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.job_title}"


class VisaAppointment(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Appointment Details
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()

    # Visa Details
    country_of_origin = models.CharField(max_length=50)
    main_purpose = models.TextField()

    # Additional Information
    additional_comments = models.TextField(blank=True, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date} {self.preferred_time}"
