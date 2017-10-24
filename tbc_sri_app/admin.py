from django.contrib import admin
#from .models import lnos_statusPipeLine
from .resources import lnos_statusPipeLineResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(lnos_statusPipeLine)
from .models import lnos_statusPipeLine

@admin.register(lnos_statusPipeLine)
class lnos_statusPipeLineAdmin(ImportExportModelAdmin):
    list_display = ('mbol', 'hbol', 'container', 'customs_released', 'eta_pod', 'unloaded_from_vessel')
    resource_class = lnos_statusPipeLineResource
