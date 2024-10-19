from django.db import models


class AccountablePropertyOfficer(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class PropertyCustodianAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    primary = models.ForeignKey(
        'PropertyCustodian', related_name='primary_accounts', on_delete=models.SET_NULL, null=True, blank=True
    )
    alternate = models.ForeignKey(
        'PropertyCustodian', related_name='alternate_accounts', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return str(self.account_number)


class UnitInformationCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.code


class PropertyCustodian(models.Model):
    section = models.CharField(max_length=100)
    property_custodian_account = models.ForeignKey(
        PropertyCustodianAccount, on_delete=models.SET_NULL, null=True, related_name='custodians'
    )
    uic = models.ForeignKey(
        UnitInformationCode, on_delete=models.SET_NULL, null=True, related_name='property_custodians'
    )
    inventory_date = models.DateField()
    primary_or_alternate = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    date_trained = models.DateField()
    date_received_appointment_letter = models.DateField()
    phone = models.CharField(max_length=15)
    accountable_property_officer = models.ForeignKey(
        AccountablePropertyOfficer, related_name='accounts', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name


class Asset(models.Model):
    accountable_uic = models.ForeignKey(
        UnitInformationCode, on_delete=models.SET_NULL, null=True, related_name='accountable_assets'
    )
    asset_id = models.CharField(max_length=100, unique=True)
    attachment = models.BooleanField(default=False)
    property_custodian_account = models.ForeignKey(
        PropertyCustodianAccount, related_name='assets', on_delete=models.SET_NULL, null=True, blank=True
    )
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
    sub_custodian_number = models.CharField(max_length=100, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    unit_of_issue = models.CharField(max_length=100)
    uic = models.ForeignKey(UnitInformationCode, on_delete=models.SET_NULL, null=True, related_name='assets')
    building_number = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    cube_number = models.IntegerField()
    year_service_life = models.IntegerField()
    dlads = models.BooleanField(default=False)
    ok = models.BooleanField(default=True)
    classification = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.asset_id
