from django import forms

# Create your forms here.
class ContactUsForm(forms.Form):
	SENDER_CHOICES = (
		('cus', 'Customer'),
		('oth', 'Other'),
	)
	REC_CHOICES=(
		('rec', 'Recommendation'),
		('cmp', 'Complaint'),
	)

	first_name = forms.CharField(required=False, max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'First Name...', 'class' : 'form-control'}))
	last_name = forms.CharField(required=False, max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Last Name...', 'class' : 'form-control'}))
	sender = forms.ChoiceField(required=True, choices=SENDER_CHOICES,
		widget=forms.Select(attrs={'class' : 'form-control'}))
	recom = forms.ChoiceField(required=True, label='recom', choices=REC_CHOICES,
		widget=forms.Select(attrs={'class' : 'form-control'}))
	phone_number = forms.IntegerField(required=False,
		widget=forms.NumberInput(attrs={'placeholder': 'Phone Number...', 'class' : 'form-control'}))
	email = forms.EmailField(required=True,
		widget=forms.TextInput(attrs={'placeholder': 'E-Mail...', 'class' : 'form-control'}))
	subject = forms.CharField(required=True, max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Subject...', 'class' : 'form-control'}))
	message = forms.CharField(required=True, max_length=500,
		widget=forms.Textarea(attrs={'placeholder': 'Enter Message Here...', 'class' : 'form-control'}))