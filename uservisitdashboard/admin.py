from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserVisit


#admin.site.register(UserVisit)
@admin.register(UserVisit)
class UserVisitAdmin(ImportExportModelAdmin):
    pass


