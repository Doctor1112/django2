from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='event_images/')
    data = models.DateTimeField()