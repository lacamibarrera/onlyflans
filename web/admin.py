from django.contrib import admin
from .models import Flan, ContactFormModelForm


@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'flan_uuid', 'is_private')  
    search_fields = ('name', 'description')  
    prepopulated_fields = {"slug": ("name",)}  


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('contact_form_uuid', 'customer_name', 'customer_email', 'message')
    search_fields = ('customer_name', 'custumer_email')
    readonly_fields = ('contact_form_uuid',)

admin.site.register(ContactFormModelForm, ContactFormAdmin)



