from django.contrib import admin

from measurements.models import Project, Measurement


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'project', 'created_at', 'updated_at')
    list_display_links = ('id', 'value')
    search_fields = ('id', 'value')
