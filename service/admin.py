from django.contrib import admin
from service.models import servicedata
class serviceadmin(admin.ModelAdmin):
    pass
admin.site.register(servicedata,serviceadmin)
# Register your models here.
