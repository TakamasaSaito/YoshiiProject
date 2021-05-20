from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    companyname = models.CharField(max_length=100)
    outline = models.TextField(max_length=1000)

    # タイトルを返す
    def __str__(self):
        return self.companyname