
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


'''
class MyForm(forms.Form):
	#here MyForm is a subclass of forms.Form 
	#let's create a ChoiceField
	#choicefield has some parameters let's review them
	cnt=[
            ('Понедельник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Вторник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Среда', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),   
    ('Четверг', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),  
    ('Пятница', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )),
]                

	
	c_field=forms.ChoiceField(\
		required=True,\
		label='Enter Country',\
		label_suffix='>>>',\
		initial='none',\
		help_text='choose the country',\
		error_messages={'required':'Please enter your country info', 'invalid_choice': 'Please select a valid one'},\
		disabled=False,
		
		choices=cnt,
	)


class MyForm(forms.Form):
    
        cnt = [
    ('Понедельник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Вторник', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),
    ('Среда', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),   
    ('Четверг', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )
    ),  
    ('Пятница', (
            ('10:00', '10:00'),
            ('12:00', '12:00'),
            ('15:00', '15:00'),
            ('17:00', '17:00'),
                    )),
]

'''

'''
from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    '''