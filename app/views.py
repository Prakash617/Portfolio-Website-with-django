from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
from app.form import contactform
from django.core.mail import send_mail
from app.models import AboutMe, Myteam
# Create your views here.

class homeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = Myteam.objects.all()
        aboutme= AboutMe.objects.all()
        
        context = {'teams':teams, 'aboutme':aboutme[0]}
    
        return context

    
class okView(TemplateView):
    template_name = "ok.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['m'] = 'success'
        return context
    
    
    
class workView(TemplateView):
    template_name = "work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
    
        return context

    
def cform(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            email_to= form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_to,email_from]
            send_mail( subject,message,email_from , [recipient_list[1]] ,fail_silently=False)
            send_mail( subject,'Prakash Thapa: Thanks for contacting us',email_from , [recipient_list[0]] ,fail_silently=False)
        # send_mail( subject, message, email_from, recipient_list )
           
            
            return redirect('/ok/')
    # else:
    #     form = contactform()
    #     context = { 'form' : form}
    # return render(request,'contactform.html', context)