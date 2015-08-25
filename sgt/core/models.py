from django.db import models
from django.conf import settings


class Payment(models.Model):
    month = models.DateField()
    dbv = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='payments'
    )
    status_payment = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['month']

    def __str__(self):
        return ('{} - {}'.format(self.month, self.dbv))


class Team(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='unity_profile_images', blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
