from django.db import models


class Asset(models.Model):
    accountable_uic = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100, unique=True)
    attachment = models.BooleanField(default=False)
    custodian_number = models.CharField(max_length=100)
    item_description = models.TextField()
    location = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=255)
    manufacturer_part_number = models.CharField(max_length=255)
    manufacturer_year = models.IntegerField()
    manufacturer_model_number = models.CharField(max_length=255)
    quantity = models.IntegerField()
    serial_number = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    stock_number = models.CharField(max_length=100)
    sub_custodian_number = models.CharField(max_length=100)
    sub_location = models.CharField(max_length=100)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    unit_of_issue = models.CharField(max_length=100)
    uic = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    cube_number = models.IntegerField()
    year_service_life = models.IntegerField()
    dlads = models.BooleanField(default=False)
    ok = models.BooleanField(default=True)
    classification = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
