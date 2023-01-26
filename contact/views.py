from django.views.generic import CreateView

from contact.models import Contact


class ContactUs(CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    fields = ['email', 'first_name', 'middle_name', 'lastname', 'message', ]
