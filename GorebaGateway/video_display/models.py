from django.db import models


class YouTubeVideos(models.Model):
    # Video Information
    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    video_url = models.URLField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video_title
