from django.forms import ModelForm

from .models import FileClaimVehicleTheft
# Create your forms here.
class FileClaimVehicleTheftForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
			'placeholder': 'Full Name',
			'class': 'form-control'
		})
		self.fields['occupation'].widget.attrs.update({
			'placeholder': 'Occupation/Job',
			'class': 'form-control'
		})
		self.fields['phone_number'].widget.attrs.update({
			'placeholder': 'Phone Number',
			'class': 'form-control'
		})
		self.fields['email'].widget.attrs.update({
			'placeholder': 'E-Mail Address',
			'class': 'form-control'
		})

	class Meta:
		model = FileClaimVehicleTheft
		fields = '__all__'




	# TRUE_FALSE_CHOICES = (
	# 	(True, 'Yes'),
	# 	(False, 'No'),
	# )

	# MANUFACTURED_YEAR_CHOICES = (
	# 	(1970, '1970'),
	# 	(1980, '1980'),
	# 	(1990, '1990'),
	# 	(2000, '2000'),
	# 	(2010, '2010'),
	# 	(2020, '2020')
	# )

	# CAR_MODEL_CHOICES = (
	# 	('toyota', 'Toyota'),
	# )

	# name = forms.CharField(required=False, max_length=100,
		# widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class' : 'form-control'}))
	# occupation = forms.CharField(required=False, max_length=100,
	# 	widget=forms.TextInput(attrs={'placeholder': 'Occupation', 'class' : 'form-control'}))
	# phone_number = forms.IntegerField(required=False,
	# 	widget=forms.NumberInput(attrs={'placeholder': 'Enter Your Phone Number', 'class' : 'form-control'}))
	# email = forms.EmailField(required=False,
	# 	widget=forms.TextInput(attrs={'placeholder': 'Enter Your E-Mail', 'class' : 'form-control'}))

	# vehicle_registration = forms.CharField(required=False, max_length=100,
	# 	widget=forms.TextInput(attrs={'placeholder': 'Vehicle Registration Number', 'class' : 'form-control'}))

	# vehicle_make = forms.ChoiceField(required=True, choices=CAR_MODEL_CHOICES, initial='',
	# 	widget=forms.Select(attrs={'class' : 'form-control'}))
	# manufactured_year = forms.ChoiceField(required=True, choices=MANUFACTURED_YEAR_CHOICES, initial='',
	# 	widget=forms.Select(attrs={'class' : 'form-control'}))

	# hp_loan_agreements = forms.ChoiceField(required=True, choices=TRUE_FALSE_CHOICES, label="Some Label", initial='',
	# 	widget=forms.Select(attrs={'class' : 'form-control'}))