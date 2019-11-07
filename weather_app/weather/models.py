from django.db import models

class town(models.Model):

    name = models.CharField(max_length=26)

    def __str__(self):

        return self.name

    class Meta:

        verbose_name_plural = 'cities'

