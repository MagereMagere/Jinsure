from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactUsForm

# Create your views here.
def home_page(request):

	context = {
	}
	return render(request, 'home/pages/home.html', context)

def contact_page(request):
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid:
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactUsForm()

	context = {
		'contact_form': form
	}
	return render(request, 'home/pages/contact.html', context)