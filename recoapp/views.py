from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.views.generic.edit import FormView

from .models import Attachment


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


def list(request):

    if request.method == "POST":
        parent_id = request.POST['parent_id']
        files = request.FILES.getlist('myfiles')
        for a_file in files:
            instance = Attachment(
                parent_id=parent_id,
                file_name=a_file.name,
                attachment=a_file
            )
            instance.save()
            print(a_file.name)

        return render(request,'add_attachment_done.html')

    return render(request, "add_attachment.html")


# def add_attachment_done(request):
#     return render_to_response('add_attachment_done.html')

