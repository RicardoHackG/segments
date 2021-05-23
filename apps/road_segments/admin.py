from django.contrib import admin
from django.contrib.gis.db import models
from leaflet.admin import LeafletGeoAdmin
from leaflet.forms.widgets import LeafletWidget

from .models import (
    Record,
    Segment,
)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('get_segment_name', 'average_speed', 'intensity', 'characterization')

    def get_segment_name(self, obj):
        return obj.segment.name

    get_segment_name.short_description = 'Segment'


@admin.register(Segment)
class SegmentAdmin(LeafletGeoAdmin):
    formfield_overrides = {
        models.PointField: {'widget': LeafletWidget},
    }
