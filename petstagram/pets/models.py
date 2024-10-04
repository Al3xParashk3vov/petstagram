from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True)    # new

    def save(self, *args, **kwargs):
        # Промяна
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        # Запазване в базата
        super().save(*args, **kwargs)