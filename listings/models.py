from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) 
  # ^^^ 'models.DO_NOTHING' won't delete the listing if the realtor gets deleted
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)  # 'blank=True' means that this field is NOT required
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)  # Limits bathrooms to 2 digits, 1 decimal
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=2)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title