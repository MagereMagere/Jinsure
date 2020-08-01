from django import forms

# Create your forms here.
class VehicleQuoteForm(forms.Form):
	CAR_VALUE_CHOICES = (
		('1', '1 million'),
		('2', '2 million'),
		('3', '3 million'),
	)
	VEHICLE_TYPE_CHOICES=(
		('5', 'Heavy-commercial vehicle'),
		('1', 'saloon'),
	)
	DRIVING_EXPERIENCE=(
		('1', 'one'),
		('2', 'two'),
		('3', 'three'),
		('4', 'four'),
		('5', 'five'),
		('6', '6 & more'),
	)

	name = forms.CharField(required=False, max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name', 'class' : 'form-control'}))
	phone_number = forms.IntegerField(required=False,
		widget=forms.NumberInput(attrs={'placeholder': 'Enter Your Phone Number', 'class' : 'form-control'}))
	email = forms.EmailField(required=False,
		widget=forms.TextInput(attrs={'placeholder': 'Enter Your E-Mail', 'class' : 'form-control'}))
	value = forms.ChoiceField(required=True, choices=CAR_VALUE_CHOICES,
		widget=forms.Select(attrs={'class' : 'form-control'}))
	vtype = forms.ChoiceField(required=True, choices=VEHICLE_TYPE_CHOICES,
		widget=forms.Select(attrs={'class' : 'form-control'}))
	experience = forms.ChoiceField(required=True, choices=DRIVING_EXPERIENCE,
		widget=forms.Select(attrs={'class' : 'form-control'}))