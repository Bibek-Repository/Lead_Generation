from django.db import models

class Lead(models.Model):

    INTEREST_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    company = models.CharField(max_length=150, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)

    interest_level = models.CharField(
        max_length=10,
        choices=INTEREST_CHOICES,
        default='low'
    )

    score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name