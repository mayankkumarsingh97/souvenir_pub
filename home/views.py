from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import *

# Create your views here.


def home(request):
    abc= catalog.objects.all()
    context = {

        'abc':abc,
    }
    return render(request, "index.html",context)


def aboutus(request):
    abc= catalog.objects.all()
    context = {
        'abc':abc,

    }
    return render(request, "aboutus.htm",context)



def sendemail(request):
    form = contactUsForm(request.POST or None)
    if form.is_valid():

        data = form.cleaned_data



        email = form.cleaned_data.get('email')
        print(email,"email is here")


        form.save()


        # to me
        sg = sendgrid.SendGridClient('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')
        email_to = email

        message = sendgrid.Mail()
        message.add_to([email_to])
        message.set_subject(str("From website"))

        message.add_substitution('-name-',first_name)

        message.set_html(' ')
        message.set_text(' ')
        message.add_filter('templates', 'enable', 1)
        message.add_filter('templates', 'template_id', 'f93135a2-6d10-49a8-af45-68daf8cf2c36')

        message.set_from('enquiry@dreambox.cloud')
        status, msg = sg.send(message)

        print('status1=====',status)
        print('msg1=====',msg)

        # tomeeeeeeeeeeee
        sg1 = sendgrid.SendGridClient('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')
        email_to2 = "enquiry@dreambox.cloud"
        message_2 = sendgrid.Mail()
        message_2.add_to([email_to2])
        message_2.set_subject(str(first_name)+" - "+str(phone))
        message_2.set_html(' ')
        message_2.set_text(' ')
        message_2.add_substitution('-name-',first_name)
        message_2.add_substitution('-email-', email)
        message_2.add_substitution('-phone-',phone)
        message_2.add_substitution('-message-',message_1)



        message_2.set_from('enquiry@dreambox.cloud')
        message_2.add_filter('templates', 'enable', 1)
        message_2.add_filter('templates', 'template_id', '56db9825-4018-4ad7-962e-eef6a7914840')

        status1, msg1 = sg1.send(message_2)
        print('status2=====',status1)
        print('msg2=====',msg1)

        if status == 200:
            print("successfully")
        else:
            print('wrong')

        return redirect('home:thankyou')

    context={}
    return render(request, 'index.html',context)

def thankyou(request):
    context={
        'msg': "Worked"
    }
    return render(request, 'thankyou.html' ,context)
