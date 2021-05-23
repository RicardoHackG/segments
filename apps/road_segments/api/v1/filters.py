from django_filters import filters, FilterSet

from apps.road_segments.models import Segment


class SegmentFilter(FilterSet):
    latest_segment_characterization = filters.Filter(field_name='latest_segment_characterization')

    class Meta:
        model = Segment
        fields = ['latest_segment_characterization', ]
