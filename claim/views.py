from django.shortcuts import render
from django.contrib import messages

# pdf
import weasyprint
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings

from .forms import FileClaimVehicleTheftForm

# Create your views here.
def claim(request):
	if request.method == 'POST':
		theft_form = FileClaimVehicleTheftForm(request.POST)
		if theft_form.is_valid:
			name = theft_form.cleaned_data['name_of_insured']
			occupation = theft_form.cleaned_data['occupation_of_insured']
			phone_number = theft_form.cleaned_data['phone_number_of_insured']
			email = theft_form.cleaned_data['email_of_insured']
			vehicle_registration = theft_form.cleaned_data['vehicle_registration']
			vehicle_make = theft_form.cleaned_data['vehicle_make']
			manufactured_year = theft_form.cleaned_data['manufactured_year']

			theft_form.save()
			# messages.add_message(request, messages.INFO, 'Feedback Submitted.')

			html = render_to_string('claim/cars/pdf.html', {'theft_form': theft_form})
			response = HttpResponse(content_type='application/pdf')
			response['Content-Disposition'] = 'filename="theft_claim.pdf"'
			weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
			return response
	else:
		theft_form = FileClaimVehicleTheftForm()

	context = {
		'theft_form': theft_form
	}
	return render(request, 'claim/cars/car_claim.html', context)