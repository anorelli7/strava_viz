from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from .models import Workout


class WorkoutForm(forms.Form):
	"""Form Object"""
	submitter = forms.CharField('Your Name')
	location = forms.CharField('Where was your workout?')
	date = forms.DateTimeField('When was your workout?')
	miles = forms.FloatField('How many miles did you go?')
	workout_type = forms.ForeignKey('Which type of workout?')
	vertical_ascent = forms.IntField('How many feet did you climb?')
	