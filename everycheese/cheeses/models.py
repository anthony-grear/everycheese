from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel 

class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255) 
    slug = AutoSlugField("Cheese Address", 
        unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True) 
    
    class Firmness(models.TextChoices): 
        UNSPECIFIED = "UNSPECIFIED", "Unspecified"
        SOFT = "SOFT", "Soft" 
        SEMI_SOFT = "SEMI-SOFT", "Semi-Soft" 
        SEMI_HARD = "SEMI-HARD", "Semi-Hard" 
        HARD = "HARD", "Hard" 

    firmness = models.CharField("Firmness", max_length=20,
        choices=Firmness.choices, default=Firmness.UNSPECIFIED) 

    def __str__(self):
        return self.name