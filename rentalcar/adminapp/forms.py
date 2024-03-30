from .models import Booking, usermanage
from django import forms

#-------------for signin-----------#
class userform(forms.ModelForm):
    class Meta:
        model=usermanage
        fields='__all__'

# ---------for booking--------#
class bookform(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['Name','model','Rental_start_date','Rental_end_date','pickuplocation','Dropoflocation']
        widgets={
            'Rental_start_date':forms.DateInput(attrs={'type':'date'}),
            'Rental_end_date':forms.DateInput(attrs={'type':'date'})
        }
        