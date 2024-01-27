from ckeditor.fields import RichTextField
from django.db import models


class Core(models.Model):
    BUSINESS_STATUS = (
        ('OPEN', 'OPEN'),
        ('CLOSE', 'CLOSE'),
        ('MAINTENANCE', 'MAINTENANCE'),
    )

    # Business related
    business_title = models.CharField(
        max_length=100,
        default='Expert Advice, Visa Guidance, and Success Stories',
    )
    business_name = models.CharField(max_length=20, default='Goreba Gateway')
    company = models.CharField(max_length=20, default='Goreba')
    keywords = models.CharField(
        blank=True,
        max_length=500,
        default=''
    )
    short_description = models.CharField(
        blank=True,
        max_length=50,
        default=''
    )
    story_headline = models.CharField(
        blank=True, max_length=20, default='Goreba Gateway ~ Prologue')
    business_story = RichTextField(blank=True)
    phone = models.CharField(
        blank=True, max_length=20, default='+1 (514) 258 7260')
    address = models.CharField(
        blank=True, max_length=50, default='153 Cresthaven Dr. Nepean, ON, K2G 6T2 Canada')
    email = models.CharField(
        blank=True, max_length=20, default='goreba.gateway@gmail.com')
    status = models.CharField(max_length=15, choices=BUSINESS_STATUS)

    # Logo and images
    icon = models.ImageField(blank=True, upload_to='images/goreba/')
    business_logo = models.ImageField(blank=True, upload_to='images/goreba/')
    business_banner = models.ImageField(blank=True, upload_to='images/goreba')

    # Social media related
    facebook_link = models.CharField(
        max_length=50, default='https://www.facebook.com/goreba.gateway')
    instagram_link = models.CharField(
        max_length=50, default='https://www.instagram.com/goreba.gateway/')
    twitter_link = models.CharField(
        max_length=50, default='https://twitter.com/goreba_canada')
    youtube_link = models.CharField(
        max_length=75, default='https://www.youtube.com/@GorebaGateway')
    linkedin_link = models.CharField(
        max_length=50, default='https://www.linkedin.com/company/goreba-gateway')
    tiktok_link = models.CharField(
        max_length=50, default='https://tiktok.com/@goreba_gateway')

    # Email servers
    smtp_server = models.CharField(blank=True, max_length=50)
    smtp_email = models.CharField(blank=True, max_length=50)
    smtp_password = models.CharField(blank=True, max_length=10)
    smtp_port = models.CharField(blank=True, max_length=5)

    # Store policies
    return_policy = RichTextField(blank=True)
    privacy_policy = RichTextField(blank=True)
    cookie_policy = RichTextField(blank=True)

    # Announcements
    announcements = RichTextField(blank=True)
    message_to_viewers = RichTextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
