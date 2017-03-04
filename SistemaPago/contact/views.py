from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
	title = 'Contacto'
	form = contactForm(request.POST or None)
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Mensaje desde MISITIO.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		title = 'Gracias!'
		confirm_message = "Gracias por el mensaje. Nos contactaremos contigo más tarde."
		form = None

	context = {'title': title,'form': form, 'confirm_message': confirm_message, }
	template = 'contact.html'
	return render(request, template, context)