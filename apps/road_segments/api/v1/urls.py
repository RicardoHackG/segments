from django.urls import path
from rest_framework import routers

from apps.road_segments.api.v1.views import (
    RecordAPIView,
    SegmentAPIView,
)

router = routers.SimpleRouter()
app_name = 'road_segment'

urlpatterns = [
                  path('record/', RecordAPIView.as_view(), name='record'),
                  path('segment/', SegmentAPIView.as_view(), name='segment'),
              ] + router.urls
