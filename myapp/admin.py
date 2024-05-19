from django.contrib import admin

# Register your models here.
from .models import user_login
from .models import staff_details, customer_details, designation_master, category_master
from .models import quotation_master, quotation_details, quotation_reply
from .models import messages, contact_us

admin.site.register(user_login)
admin.site.register(staff_details)
admin.site.register(customer_details)
admin.site.register(designation_master)
admin.site.register(category_master)
admin.site.register(quotation_master)
admin.site.register(quotation_details)
admin.site.register(quotation_reply)
admin.site.register(messages)
admin.site.register(contact_us)