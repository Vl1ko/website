# from django.contrib import admin
# from .models import Response



# admin.site.register(Response)

from django.contrib import admin
from .models import Response
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# класс обработки данных
class ResponseResource(resources.ModelResource):

    class Meta:
        model = Response

# вывод данных на странице
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [ResponseResource]

admin.site.register(Response, BookAdmin)