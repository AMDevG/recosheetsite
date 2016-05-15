from django.shortcuts import render
from django.core.mail import send_mail

def reco(request):
	return render(request, 'index1.html')# Create your views here.


def success(request):

    if request.method == 'POST':
        name_text = request.POST.get('name', None)
        email_text = request.POST.get('mail', None)
        message_text = request.POST.get('message', None)

        print(name_text)
        print(email_text)

        send_mail('New Reco Sheet', message_text,"bprecosheet@gmail.com",
        ['jeberry308@gmail.com'], fail_silently=False)


        return render(request, 'success.html')

    else:
    	return HttpResponse("Sorry nothing entered")