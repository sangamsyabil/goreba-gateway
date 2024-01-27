from django.db import models

class Consultant(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

class Appointment(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()

    def __str__(self):
        return f"{self.user_name} - {self.consultant.name}"
