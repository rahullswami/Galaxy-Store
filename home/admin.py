from django.contrib import admin
from .models import *

admin.site.register(ProdBooking)
admin.site.register(Contact)

class ProdImageAdmin(admin.StackedInline):
    model = Prod_Image

class ProdAdmin(admin.ModelAdmin):
    inlines = [ProdImageAdmin]

admin.site.register(Prod,ProdAdmin)
admin.site.register(Prod_Image)