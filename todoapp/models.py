from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/" , blank=True , null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title[ : 40 ]

# Create your models here.
