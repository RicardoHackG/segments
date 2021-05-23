from django.db.models import Subquery, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.road_segments.models import Record, Segment
from .filters import SegmentFilter
from .serializers import (
    RecordSerializer,
    SegmentSerializer
)


class RecordAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class SegmentAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SegmentFilter

    def get_queryset(self):
        # annotate the latest characterization for each Segment
        latest_record_characterization = Subquery(
            Record.objects.filter(segment_id=OuterRef("id")).order_by("-id").values('characterization')[:1])

        queryset = self.queryset.annotate(
            latest_segment_characterization=latest_record_characterization,
        )

        return queryset
