from django.contrib import admin
from polls.models import Details,person

# Register your models here.
admin.site.register(person)
admin.site.register(Details)