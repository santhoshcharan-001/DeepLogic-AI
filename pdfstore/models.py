from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Pdf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="pdfs")
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdf.name

    def get_file_name(self):
        return self.pdf.name.split("/")[-1].split(".")[0]

    def get_absolute_url(self):
        return reverse("pdf_detail", kwargs={"pk": self.pk})
