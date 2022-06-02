
from django.db import models
class ConsumptionItem(models.Model):
    productName = models.TextField()

class ListingItem(models.Model):
    ReadeyProductName = models.TextField()
    ApproximateProductLifeMin = models.TextField()
    ApproximateProductLifeMax = models.TextField()