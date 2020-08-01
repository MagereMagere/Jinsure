from django.shortcuts import render

# Create your views here.
def claim(request):

	context = {}
	return render(request, 'claim/cars/car_claim.html', context)