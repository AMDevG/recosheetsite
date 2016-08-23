from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage

def reco(request):
	return render(request, 'index.html')

def success(request):

    if request.method == 'POST':
        trans_name = request.POST.get('transName', None)
        delivery_type = request.POST.get('deliveryType', None)
        city_name = request.POST.get('cityName', None)
        state_name = request.POST.get('stateName', None)
        num_units = request.POST.get('numUnits', None)
        care_type = request.POST.getlist('careType',None)
        orig_lead = request.POST.get('origLead', None)
        prod_lead = request.POST.get('prodLead', None)
        due_date = request.POST.get('dueDate', None)
        message_text = request.POST.get('message', None)



        subject = "New Reco Sheet - " + str(trans_name) 

        email_text = "Transaction Name: " + str(trans_name) + '\n' + "Delivery Type: " + str(delivery_type) + '\n' + "City: " + str(city_name) + '\n' + "State: " + str(state_name) + '\n' + "Care Type: " + str(care_type) + '\n' + "Origination Lead: " + str(orig_lead)  + '\n' + "Expected Delivery: " + str(due_date) + '\n' + "Transaction Notes: " + str(message_text)

        email_reco = EmailMessage(subject, email_text, "bprecosheet@gmail.com", ['jeberry308@gmail.com'])

        # for f in request.FILES.getlist('due_dil'):
        #     print("got: ", f)
        #     email_reco.attach(f, f.read(), f.content_type)

        # for filename, file in request.FILES.iteritems():
        #     name = request.FILES[filename].name

        #     print(name)

        attach = request.FILES['due_dil']

        email_reco.attach(attach.name, attach.read(), attach.content_type)
    
        email_reco.send()

       # send_mail('New Reco Sheet - ' + trans_name, email_reco,"bprecosheet@gmail.com",
       # ['jeberry308@gmail.com'], fail_silently=False)


        return render(request, 'success.html')

    else:
    	return HttpResponse("Sorry nothing entered")