from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic.edit import FormView


from .models import Document
from .forms import DocumentForm
from django.http import Http404

def reco(request):
	return render(request, 'index.html')

# def success(request):

#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)

#         print(form)

#         print("ran pass form")

#         if form.is_valid():

#             print("form is valid")
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()

           

#             email_reco = EmailMessage("File Test", "Test", "bprecosheet@gmail.com", ['jeberry308@gmail.com'])

#            # email_reco.attach(newdoc)

#             email_reco.send()

#             return HttpResponseRedirect(reverse(''))
    
#     else:

#         raise Http404  # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render(
#         request,
#         'list.html',
#         {'documents': documents, 'form': form}
#     )


    # else:
    #     return HttpResponse("Sorry nothing entered")

    # if request.method == 'POST':
    #     trans_name = request.POST.get('transName', None)
    #     delivery_type = request.POST.get('deliveryType', None)
    #     city_name = request.POST.get('cityName', None)
    #     state_name = request.POST.get('stateName', None)
    #     num_units = request.POST.get('numUnits', None)
    #     care_type = request.POST.getlist('careType',None)
    #     orig_lead = request.POST.get('origLead', None)
    #     prod_lead = request.POST.get('prodLead', None)
    #     due_date = request.POST.get('dueDate', None)
    #     message_text = request.POST.get('message', None)



    #     subject = "New Reco Sheet - " + str(trans_name) 

    #     email_text = "Transaction Name: " + str(trans_name) + '\n' + "Delivery Type: " + str(delivery_type) + '\n' + "City: " + str(city_name) + '\n' + "State: " + str(state_name) + '\n' + "Care Type: " + str(care_type) + '\n' + "Origination Lead: " + str(orig_lead)  + '\n' + "Expected Delivery: " + str(due_date) + '\n' + "Transaction Notes: " + str(message_text)

    #     email_reco = EmailMessage(subject, email_text, "bprecosheet@gmail.com", ['jeberry308@gmail.com'])

    #     # for f in request.FILES.getlist('due_dil'):
    #     #     print("got: ", f)
    #     #     email_reco.attach(f, f.read(), f.content_type)

    #     # for filename, file in request.FILES.iteritems():
    #     #     name = request.FILES[filename].name

    #     #     print(name)

    #     attach = request.FILES['due_dil']

    #     email_reco.attach(attach.name, attach.read(), attach.content_type)
    
    #     email_reco.send()

       # send_mail('New Reco Sheet - ' + trans_name, email_reco,"bprecosheet@gmail.com",
       # ['jeberry308@gmail.com'], fail_silently=False)


    #     return render(request, 'success.html')

    # else:
    # 	return HttpResponse("Sorry nothing entered")


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('recoapp:list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'index.html',
        {'documents': documents, 'form': form}
    )


