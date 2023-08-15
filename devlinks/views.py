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
        title_email = request.POST['title']
        send_mail(
            'title', # titulo
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )

    return render(request, 'index.html')
    # template_name = "links.html"

def downloadpdf(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    thefile = 'AllanDiamanteCV.pdf'
    file_path = os.path.join(BASE_DIR, 'files', thefile)
    filename = os.path.basename(thefile)
    chunk_size = 8192

    response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(file_path)[0])
    response['Content-Length'] = os.path.getsize(file_path)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    return response