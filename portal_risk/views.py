from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import VehicleQuoteForm

# Create your views here.
def risk_assessment(request):
	if request.method == 'POST':
		form = VehicleQuoteForm(request.POST)
		if form.is_valid:
			return HttpResponseRedirect('/thanks/')
	else:
		form = VehicleQuoteForm()

	context = {
		'quote_form': form
	}
	return render(request, 'risk_portal/risk/risk.html', context)