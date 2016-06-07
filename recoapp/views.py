from django.shortcuts import render
from django.core.mail import send_mail

def reco(request):
	return render(request, 'index.html')# Create your views here.


def success(request):

    if request.method == 'POST':
        trans_name = request.POST.get('transName', None)
        delivery_type = request.POST.get('deliverType', None)
        city_name = request.POST.get('cityName', None)
        state_name = request.POST.get('stateName', None)
        num_units = request.POST.get('numUnits', None)
        care_type = request.POST.get('careType',None)
        orig_lead = request.POST.get('origLead', None)
        prod_lead = request.POST.get('prodLead', None)
        due_date = request.POST.get('dueDate', None)
        message_text = request.POST.get('message', None)

        email_reco = "Transaction Name: " + trans_name + '\n' + "Delivery Type: " + delivery_type + '\n' + "City: " + city_name + "State Name: " + state_name + '\n' + "Care Type: " + care_type + '\n' + "Origination Lead: " + orig_lead  + '\n' + "Production Lead: " + prod_lead + '\n' + "Expected Delivery: " + due_date + '\n' + "Transaction Notes: " + message_text 



        send_mail('New Reco Sheet - ' + trans_name, email_reco,"bprecosheet@gmail.com",
        ['jeberry308@gmail.com'], fail_silently=False)


        return render(request, 'success.html')

    else:
    	return HttpResponse("Sorry nothing entered")