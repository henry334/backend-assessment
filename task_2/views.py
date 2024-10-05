from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            pass
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})