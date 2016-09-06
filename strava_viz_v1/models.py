from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Workout(models.Model):
	user = models.CharField(max_length=15)
	location = models.CharField(max_length=55)
	date = models.DateTimeField()
	miles = models.FloatField()
	workout_type = models.ForeignKey('WorkoutType', on_delete=models.CASCADE)
	vertical_ascent = models.IntField()

class WorkoutType(models.Model):
	RUN = 'RUN'
	BIKE = 'BIKE'
	SWIM = 'SWIM'