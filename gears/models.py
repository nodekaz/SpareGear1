from __future__ import unicode_literals

from django.db import models



type_choices=(
    ('','--'),
    ('car','car gears'),
    ('home','home gears'),
    ('electroics', 'electronic gears'),
    ('computers', 'computer gears'),
    ('office', 'office equipment gears'),
    ('medical', 'medical equipment gears'),
)

quality_choices=(
    ('','--'),
    ('E','excellent'),
    ('G','good'),
    ('B','bad'),
)
class Gear (models.Model):
    gear_type = models.CharField (max_length=100, choices=type_choices)
    gear_producer = models.CharField (max_length=100)
    gear_name = models.CharField (max_length=100)
    gear_model = models.CharField (max_length=100)
    gear_date = models.CharField (max_length=100)
    gear_quality = models.CharField (max_length=100, choices=quality_choices)
    gear_availablity = models.BooleanField(max_length=100)
    gear_owner = models.CharField (max_length=100)
    gear_price = models.CharField (max_length=100)
    gear_image = models.FileField(null=True, blank=True)
