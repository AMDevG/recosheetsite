from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic.edit import FormView


from recoapp.models import Document
from recoapp.forms import DocumentForm
from django.http import Http404


def reco(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('recoapp:reco'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'index1.html',
        {'documents': documents, 'form': form}
    )


