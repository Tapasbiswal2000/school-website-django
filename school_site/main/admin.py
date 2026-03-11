from django.contrib import admin
from .models import Notice, Gallery ,Contact
from .models import Principal

admin.site.register(Principal)
admin.site.register(Notice)
admin.site.register(Gallery)
admin.site.register(Contact)