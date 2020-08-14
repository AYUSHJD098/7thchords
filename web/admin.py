from django.contrib import admin


from .models import *



class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'Message')

admin.site.register(Customer, CustomerAdmin)
