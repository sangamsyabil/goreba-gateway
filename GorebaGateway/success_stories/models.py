from django.db import models


class SuccessStories(models.Model):
    # Client Information
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_photo = models.ImageField(
        upload_to='success_stories/photos/', null=True, blank=True)

    # Success Story Details
    story_title = models.CharField(max_length=255)
    story_description = models.TextField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.story_title}"
