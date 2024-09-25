from django.db import models

# Create your models here.
class PLCList(models.Model):
    plc_id = models.CharField(max_length=255, unique=True)


class SlaveDevice(models.Model):
    plc_id = models.ForeignKey(PLCList, on_delete=models.CASCADE)
    slave_id = models.IntegerField()
    slave_vendor = models.CharField(max_length=255)
    slave_product = models.CharField(max_length=255)
    slave_version = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    slave_temp = models.FloatField(default=0)
    slave_status = models.BooleanField(default=False)

