from django.shortcuts import render
from .forms import ContactForm
from rest_framework.decorators import api_view
from .serializers import ContactSerializer
from django.core.mail import send_mail
from django.conf import settings

def send_admin_email(name, email, message):
    admin_email = getattr(settings, 'ADMIN_EMAIL', None)
    try:
        send_mail(
            subject='New contact form submission',
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=email,
            recipient_list=[admin_email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")

@api_view(['GET', 'POST'])
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.data) # Load the form with the post data
        if form.is_valid():
            serializer = ContactSerializer(data=form.cleaned_data) # Initialize the ContactSerializer with cleaned data from the form
            if not serializer.is_valid():
                return render(request, 'contact.html', {'form': form})
            serializer.save()
            send_admin_email(serializer.data['name'], serializer.data['email'], serializer.data['message'])
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})