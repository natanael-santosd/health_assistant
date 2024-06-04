from django.db import models
from decimal import *
from django.urls import reverse 
# Used in get_absolute_url() to get URL for specified ID
from django.db.models import UniqueConstraint 
# Constrains fields to unique values
from django.db.models.functions import Lower 
# Returns lower cased value of field
import uuid # Required for unique user id

# User Profile Model

class UserProfile(models.Model):
    """Model representing the user basic information."""
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        help_text="Unique ID for a person")    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), 
                                                   ('female', 'Female')])
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_goal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular user instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

# Health Indicators Model

class HealthIndicator(models.Model):
    """Model representing health indicators."""
    user = models.ForeignKey(UserProfile, related_name = 'user',on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_entry = models.DateField(null=True, blank=True)

    BMI_STATUS = (
        ('u', 'Underweight'),
        ('n', 'Normal Weight'),
        ('o', 'Overweight'),
        ('ob', 'Obese'),
    )

    status = models.CharField(
        max_length=2,
        choices=BMI_STATUS,
        blank=True,
        default='',
        help_text='BMI status',
    )
    
    class Meta:
        ordering = ['date_entry']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'Weight {self.date_entry}'

    def get_absolute_url(self):
        """Returns the URL to access a particular health record."""
        return reverse('health_indicator', args=[str(self.id)])
    
    def bmi_calculation(self):
        """Calculate bmi based on height and weight"""
        cm_to_m = Decimal('100.0')
        pounds_to_kg = Decimal('2.20462')
        bmi = (self.weight/pounds_to_kg)/((self.user.height_cm/cm_to_m)**2)
        return round(bmi, 2)
        
    def get_bmi_status(self):
        """Define BMI status"""
        if self.bmi is not None:
            if self.bmi < Decimal(18.5):
                return 'u'
            elif Decimal(18.5) <= self.bmi <= Decimal(24.9):
                return 'n'
            elif Decimal(25) <= self.bmi <= Decimal(29.9):
                return 'o'
            else:
                return 'ob'
        return ''
    
    def save(self, *args, **kwargs):
        """Saves the value of the bmi calculated"""
        self.bmi = self.bmi_calculation()
        self.status = self.get_bmi_status()
        super().save(*args, **kwargs)          
    
# Diet and Nutrition Model

class DietNutrition(models.Model):
    """Model representing diet and nutrition habits."""
    user = models.ManyToManyField(UserProfile)
    food = models.CharField(max_length=100, null=True, blank=True, unique=False)
    calorie_intake = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_entry = models.DateField(null=True, blank=True)
    grams_protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grams_fat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grams_carbs = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grams_fibre = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['-date_entry']      
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.food} on {self.date_entry}'

    def get_absolute_url(self):
        """Returns the URL to access a particular nutrition information."""
        return reverse('diet-detail', args=[str(self.id)])