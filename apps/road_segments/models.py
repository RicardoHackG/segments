from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from .choices import CHARACTERIZATION_CHOICES


class Segment(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    point_start = models.PointField(_('Start coordinates'), serialize=False, blank=True, null=True, spatial_index=False)
    point_end = models.PointField(_('End coordinates'), serialize=False, blank=True, null=True, spatial_index=False)

    class Meta:
        verbose_name = _('Segment')
        verbose_name_plural = _('Segments')

    def __str__(self):
        return f'{self.name}'


class Record(models.Model):
    average_speed = models.DecimalField(_('Average speed'), max_digits=11, decimal_places=8, default=0)
    intensity = models.PositiveSmallIntegerField(_('Intensity'), null=True, blank=True, default=0)
    characterization = models.CharField(_('Characterization'), choices=CHARACTERIZATION_CHOICES, max_length=20)
    segment = models.ForeignKey(Segment, related_name='segment_record', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return f'{self.segment.name}'
