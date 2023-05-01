from django.contrib import admin

from sensor.models import Sensor


class SensorAdmin(admin.ModelAdmin):
    fields = ["start_time", "end_time", "time_interval", "distance"]
    list_display = ["start_time", "end_time", "time_interval", "distance"]
    list_filter = ["start_time", "end_time", "time_interval", "distance"]
    search_fields = ["start_time", "end_time", "time_interval", "distance"]
    list_per_page = 10


admin.site.register(Sensor, SensorAdmin)
