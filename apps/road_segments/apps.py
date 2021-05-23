from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RoadSegmentsConfig(AppConfig):
    name = 'apps.road_segments'
    label = "road_segments"
    verbose_name = _("Road Segments")
