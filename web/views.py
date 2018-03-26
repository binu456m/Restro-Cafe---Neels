from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from web.models import Contact, Subscribe
from web.forms import ContactForm,SubscribeForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


def home(request):
	title = 'home'
	context = {

	'title':title

	}
	return render(request,'Neels cafe/home.html',context)

def aboutus(request):
	title ='about-us'
	conext={
	'title':title

	}
	return render(request,'Neels cafe/aboutus.html',conext)

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        forms = SubscribeForm(request.POST)
            
        if form.is_valid():

            data = form.save(commit=False)
            data.save()

            name        = form.cleaned_data['name']
            company     = form.cleaned_data['company']
            telephone   = form.cleaned_data['telephone']
            email       = form.cleaned_data['email']
            message     = form.cleaned_data['message']
            template    = 'email/email.html'

            #email for admin

            content     = "you have received a message"
            content    +="<br />Name :%s" %name
            content    +="<br />company :%s" %company
            content    +="<br />telephone:%s"%telephone
            content    +="<br />email:%s"%email
            content    +="<br />message:%s"%message
            context = {
                'name'       : name,
                'company'    : company,
                'telephone'  : telephone,
                'email'      : email,
                'message'    : message,
                'content'   : content


            }

            html_content= render_to_string(template,context)
            send_mail(
                'New message from %s through website'%name,
                'you have received a message',
                'binukrishnan456@gmail.com',
                ['binu456m@gmail.com'],
                fail_silently=False,
                html_message=html_content
                )

            #email for sender

            content="Thanks for contacting Neel's Cafe.  Our representaive will contact you soon"
            context={
                'name'       : name,
                'company'    : company,
                'telephone'  : telephone,
                'email'      : email,
                'message'    : message,
                'content'    : content

            }
            html_content=render_to_string(template,context)
            send_mail(

                "Message received from Neels Cafe",
                "Thanks for contacting Neel's Cafe.  Our representaive will contact you soon.",
                'binukrishnan456@gmail.com',
                [email],
                fail_silently=False,
                html_message=html_content
                )
            
            context = {

                'status'  :'true',
                'message' :"Contact from sucussfully completed",
                'title'   :"sucussfully completed"
                 }


            
            return HttpResponseRedirect(reverse('web:contact_us'))
        if forms.is_valid():

            data = forms.save(commit=False)
            data.save()
            
            return HttpResponseRedirect(reverse('web:contact_us'))
        
        else:   
            context = {
                "form" : form,
                "forms" : forms,
                "title" : "Error", 
            }          
            
        return render(request, 'contactus.html', context)


    else: 
        form = ContactForm()
        forms = SubscribeForm()
        
        context = {
            "form" : form,
            "forms" : forms,
            "title" : "Contact us",
            "url" : reverse('web:contact_us'),
            "redirect":True

            
        }
        return render(request, 'Neels cafe/contactus.html', context)

	