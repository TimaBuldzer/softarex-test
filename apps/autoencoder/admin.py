from django.contrib import admin

from apps.autoencoder.models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    pass
