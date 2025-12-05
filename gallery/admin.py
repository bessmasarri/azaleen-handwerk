from django.contrib import admin
from .models import HandmadeItem

@admin.register(HandmadeItem)
class HandmadeItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
