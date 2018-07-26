from django.db import models

# Create your models here.
class MachineL(models.Model):
    
    name_of_project=models.CharField(max_length=100)
    description_ml=models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_project

