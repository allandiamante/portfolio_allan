from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    if request.method == 'POST':
        message = "Sua mensagem foi enviada para o e-mail: allandiamantedesouza@gmail.com \nAgradeço o contato e retornarei o mais breve possivel.\n O conteudo da mensagem é: "
        message = message + request.POST['message']
        print(message)
        email = request.POST['email']
        title_email = request.POST['title_email']
        send_mail(
            'title_email', # titulo
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )

    return render(request, 'index.html')
    # template_name = "links.html"

def downloadpdf(request):
    print('ué')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = base_dir + '/files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),
        content_type = mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response