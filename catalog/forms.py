from django import forms

class DateForm(forms.Form):
    """Form for selecting the date for macro distribution"""
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Select Date'
    )

class WeekForm(forms.Form):
    """Form for selecting dates for weight average"""
    initial_date = forms.DateField(
        widget = forms.DateInput(attrs={'type': 'date'}),
        label='Select From'
    )
    final_date = forms.DateField(
        widget = forms.DateInput(attrs={'type': 'date'}),
        label='To'
    )    
    