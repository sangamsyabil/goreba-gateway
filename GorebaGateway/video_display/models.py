from django.db import models

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title
