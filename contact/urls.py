from django.urls import path

from contact.views import ContactUs

app_name = 'contact'

urlpatterns = [
    path('', ContactUs.as_view(), name='contact'),
]
