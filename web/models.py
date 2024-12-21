from django.db import models
import uuid
from django.contrib.auth.models import User

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    is_private = models.BooleanField(default=False)
    slug = models.SlugField(max_length=64, unique=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    popularity = models.IntegerField(default=0)  

    def __str__(self):
        return self.name

class ContactFormModelForm(models.Model):
    contact_form_uuid = models.UUIDField(default= uuid.uuid4,editable= False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length= 64)
    message = models.TextField()


class Review(models.Model):
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Reseña de {self.user} para {self.flan.name}"