from django.contrib import admin
from .models import Seller, Profile

admin.site.register(Seller)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['seller', 'bank_ac_no', 'Business_name', 'mobile', 'delivery_type']
