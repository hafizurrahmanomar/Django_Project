#Custom import

from django import forms

# For forms Variable
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985']
Choice_value = [('1', 'Python'), ('2', 'JavaScript'), ('3', 'Django')] 
Rank_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]  
 
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_email = forms.EmailField(label="Your email", max_length=100)
    
     
    #date_of_birth = forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    date_of_birth = forms.DateField(widget = forms.NumberInput(attrs={'type':'date'}))
    course_name = forms.ChoiceField(choices=Choice_value)  
    rank = forms.ChoiceField(widget = forms.RadioSelect, choices=Rank_value,required=False)  
    password = forms.CharField(widget = forms.PasswordInput())  
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':10}))
     # label_suffix
    captcha_answer = forms.IntegerField(label="2 + 2", label_suffix=" =",required=True) 
    agree = forms.BooleanField()   
  
    