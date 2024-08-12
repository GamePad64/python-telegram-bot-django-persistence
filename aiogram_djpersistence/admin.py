from django.contrib import admin

from .models import PersistentStorage


@admin.register(PersistentStorage)
class DjangoStorageAdmin(admin.ModelAdmin):
    pass
