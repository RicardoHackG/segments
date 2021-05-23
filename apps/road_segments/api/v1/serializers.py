from rest_framework import serializers

from apps.road_segments.models import Record, Segment
from drf_extra_fields.geo_fields import PointField


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class SegmentSerializer(serializers.ModelSerializer):
    point_start = PointField()
    point_end = PointField()

    class Meta:
        model = Segment
        fields = ('id', 'name', 'point_start', 'point_end')
