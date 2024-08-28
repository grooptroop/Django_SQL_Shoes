# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    position_staff = models.CharField(max_length=50)
    salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'position'


class Receipt(models.Model):
    recepit_id = models.IntegerField()
    client = models.ForeignKey('Shopper', models.DO_NOTHING, blank=True, null=True)
    date_of_purchase = models.DateField()
    time_of_purchase = models.TimeField()
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)
    final_price = models.IntegerField()
    id_number = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'receipt'


class ReceiptPosition(models.Model):
    id_position = models.IntegerField(primary_key=True)  # The composite primary key (id_position, id_receipt) found, that is not supported. The first column is selected.
    id_receipt = models.IntegerField()
    shoes = models.ForeignKey('Shoes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt_position'
        unique_together = (('id_position', 'id_receipt'),)


class Shoes(models.Model):
    id_shoes = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()
    remaining = models.IntegerField()
    cost_of_production = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shoes'


class Shopper(models.Model):
    id_client = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone_shopper = models.BigIntegerField()
    email = models.TextField()
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    favorite_shoes = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'shopper'


class SickLeave(models.Model):
    id_leave = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    code_disease = models.IntegerField()
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sick_leave'


class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, models.DO_NOTHING, blank=True, null=True)
    birthday = models.DateField()
    telephone_staff = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'staff'


class TypeVacation(models.Model):
    id_type = models.AutoField(primary_key=True)
    titels = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'type_vacation'


class Vacation(models.Model):
    id_vacation = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)
    starting_date = models.DateField()
    number_of_days = models.IntegerField()
    type = models.ForeignKey(TypeVacation, models.DO_NOTHING, blank=True, null=True)
    actual_start = models.DateField()
    actual_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'vacation'


class WorkTime(models.Model):
    id_work_time = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey(Position, models.DO_NOTHING, blank=True, null=True)
    day_work = models.IntegerField()
    month_work = models.IntegerField()
    year_work = models.IntegerField()
    monthly_salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work_time'






