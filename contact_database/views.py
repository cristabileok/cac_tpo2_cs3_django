from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        myForm = ContactForm(request.POST)
        
        if myForm.is_valid():
            InfoForm = myForm.cleaned_data
            
            newContact = Contact.objects.create(
                name= InfoForm['name'],
                age = InfoForm['age'],
                sex = InfoForm['sex'],
                email = InfoForm['email'],
                phone = InfoForm['phone'],
                comunication = InfoForm['comunication'],
                reason = InfoForm['reason'],
                message = InfoForm['message']
            )
            
            return render(request, 'contact_thanks.html')
        
    else:
        myForm = ContactForm()
        
    return render(request, 'core/contact.html', {'form':myForm})