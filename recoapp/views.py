from django.shortcuts import render
from django.core.mail import send_mail

def reco(request):
	return render(request, 'index.html')

def success(request):

    if request.method == 'POST':
        trans_name = request.POST.get('transName', None)
        delivery_type = request.POST.get('deliveryType', None)
        city_name = request.POST.get('cityName', None)
        state_name = request.POST.get('stateName', None)
        num_units = request.POST.get('numUnits', None)
        care_type = request.POST.get('careType',None)
        orig_lead = request.POST.get('origLead', None)
        prod_lead = request.POST.get('prodLead', None)
        due_date = request.POST.get('dueDate', None)
        message_text = request.POST.get('message', None)

        print("processed request")

        email_reco = "Transaction Name: " + str(trans_name) + '\n' + "Delivery Type: " + str(delivery_type) + '\n' + "City: " + str(city_name) + '\n' + "State: " + str(state_name) + '\n' + "Care Type: " + str(care_type) + '\n' + "Origination Lead: " + str(orig_lead)  + '\n' + "Expected Delivery: " + str(due_date) + '\n' + "Transaction Notes: " + str(message_text) 



        send_mail('New Reco Sheet - ' + trans_name, email_reco,"bprecosheet@gmail.com",
        ['jeberry308@gmail.com'], fail_silently=False)


        return render(request, 'success.html')

    else:
    	return HttpResponse("Sorry nothing entered")