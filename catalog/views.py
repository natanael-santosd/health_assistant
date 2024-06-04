"""Views are the heart of the web application, receiving HTTP 
requests from web clients and returning HTTP responses. 
In between, they marshal the other resources of the framework 
to access databases, render templates, etc. (MDN Web Docs).
"""
from django.shortcuts import render
from django.db.models import OuterRef, Subquery
from .models import UserProfile, HealthIndicator, DietNutrition
from datetime import date
from decimal import Decimal
from .forms import DateForm
from django.db.models import Avg

def get_most_recent():
    """Function to get the most recent indicator values."""
    
    latest_health_indicator = HealthIndicator.objects.filter(
        user=OuterRef('pk')).order_by('-date_entry')
    return latest_health_indicator

def nutrition_entries(request):
    """Get the requested values of nutrition entries for the selected date
    by the user in the form 'DateForm'.
    """
    selected_date = date.today() # default date is today
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date']
    else:
        form = DateForm(initial={'date': selected_date})
    return (form, selected_date)

def macronutrient_distribution(request):
    """Calculates the macronutrient distribution for the specified date"""
    form, selected_date = nutrition_entries(request)
    diet_entries = DietNutrition.objects.filter(date_entry=
                                                selected_date)
    
    # Create the dictionary of macronutrients
    macro_totals = {             
        'Protein': Decimal(0),
        'Fat': Decimal(0),
        'Carbs': Decimal(0),
        'Fibre': Decimal(0),
    }
    
    # For loop for populating the dictionary with the correspondent grams // of each macro

    for entry in diet_entries:
        macro_totals['Protein'] += entry.grams_protein
        macro_totals['Fat'] += entry.grams_fat
        macro_totals['Carbs'] += entry.grams_carbs
        macro_totals['Fibre'] += entry.grams_fibre
    
    total_grams = sum(macro_totals.values())    
    macronutrient = {key: (value / total_grams) * Decimal(100) 
                                 if total_grams > Decimal(0) else Decimal(0) for 
                                 key, value in macro_totals.items()} 
    return macronutrient

def calories_total():
    """Function to calculate the total calories"""
    

def index(request):
    """Main. View function for home page of site."""
    
    form, selected_date = nutrition_entries(request)

    # Subquery to get the most recent HealthIndicator for each user
    
    user_profiles = UserProfile.objects.annotate(
        latest_weight=Subquery(get_most_recent().values('weight')[:1]),
        previous_weight=Subquery(get_most_recent().values('weight')[1:]),
        latest_bmi=Subquery(get_most_recent().values('bmi')[:1]),
        latest_status=Subquery(get_most_recent().values('status')[:1])
    )
    
    latest_seven = HealthIndicator.objects.all().aggregate(Avg('weight', default=0))

    # Get the weight and BMI evolution for the current user
    
    macronutrient_percentages = macronutrient_distribution(request)
    
    # Get the weight and BMI evolution for the current user
    health_indicators = HealthIndicator.objects.order_by('date_entry')
    
    context = {
            'form': form,
            'selected_date': selected_date,
            'macronutrient_percentages': macronutrient_percentages,
            'user_profiles': user_profiles,
            'health_indicators': health_indicators,
            'latest_seven': latest_seven
        }    
        

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)