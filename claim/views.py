from django.shortcuts import render
from django.contrib import messages

# pdf
import weasyprint
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404

from .forms import FileClaimVehicleTheftForm
from .models import FileClaimVehicleTheft

# Create your views here.
def add_claim(request):
	# theft_form = FileClaimVehicleTheftForm(request.POST)

	if request.method == 'POST':
		theft_form = FileClaimVehicleTheftForm(request.POST)

		if theft_form.is_valid():
			filing=theft_form.save()

			filing = get_object_or_404(FileClaimVehicleTheft, id=17)
			html = render_to_string('claim/cars/pdf.html', {'filing': filing})
			response = HttpResponse(content_type='application/pdf')
			response['Content-Disposition'] = 'filename="theft_claim.pdf"'
			weasyprint.HTML(string=html).write_pdf(
				response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "/css/pdf.css")])
			return response
	else:
		theft_form = FileClaimVehicleTheftForm()

	context = {
		'theft_form': theft_form
	}
	return render(request, 'claim/cars/car_claim.html', context)