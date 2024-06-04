from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from django.db.models import OuterRef, Subquery
from .models import UserProfile, HealthIndicator, DietNutrition

admin.site.register(UserProfile)
admin.site.register(HealthIndicator)
admin.site.register(DietNutrition)


