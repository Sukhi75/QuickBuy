from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

MY_CHOICES = (('central', 'Central'),
              ('local', 'Local'))
class Seller(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='seller', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Profile(models.Model):
    ADD_CHOICES = (('central', 'Central'),
              ('local', 'Local'))
    seller = models.OneToOneField(Seller, related_name='profile', on_delete=models.CASCADE)
    nid_no = models.IntegerField(null=True,blank=True)
    nid_pic_front = models.ImageField(upload_to='media/nid_front/',null=True,blank=True)
    nid_pic_back = models.ImageField(upload_to='media/nid_back/',null=True,blank=True)
    bank_ac_no = models.IntegerField(null=True,blank=True)
    scan_check_leaf = models.ImageField(upload_to='media/check_leaf/',null=True,blank=True)
    Business_name = models.CharField(max_length=250, null=True,blank=True)
    scan_business_license = models.ImageField(upload_to='media/business_license/',null=True,blank=True)
    pick_up_address = models.CharField(max_length=250, null=True,blank=True)
    mobile = models.CharField(max_length=250, null=True,blank=True)
    delivery_type = MultiSelectField(choices=ADD_CHOICES,
                                     max_choices=1,null=True,blank=True)


