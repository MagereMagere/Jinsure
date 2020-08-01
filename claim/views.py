from django.shortcuts import render

from .forms import FileClaimVehicleTheftForm

# Create your views here.
def claim(request):
	if request.method == 'POST':
		theft_form = FileClaimVehicleTheftForm(request.POST)
		if theft_form.is_valid:
			return HttpResponseRedirect('/thanks/')
	else:
		theft_form = FileClaimVehicleTheftForm()

	context = {
		'theft_claim_form': theft_form
	}
	return render(request, 'claim/cars/car_claim.html', context)