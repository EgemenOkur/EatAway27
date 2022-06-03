
from django.db import models
class ConsumptionItem(models.Model):
    productName = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class ListingItem(models.Model):
    ReadeyProductName = models.TextField()
    ApproximateProductLifeMin = models.TextField()
    ApproximateProductLifeMax = models.TextField()