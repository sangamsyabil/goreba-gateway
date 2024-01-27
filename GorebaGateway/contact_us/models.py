from django.db import models

class ContactFormSubmission(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.submission_date}"
