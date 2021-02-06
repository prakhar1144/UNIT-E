from django.shortcuts import render,redirect
from .forms import Register
from django.contrib.auth import get_user_model, login
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from .utils import token_generator

#UserModel = get_user_model()



# Create your views here.

def sign_up(request):
    context = {}
    form = Register(request.POST or None)
    if request.method == "POST":
        print("Hereeeeeeeeeeeeeeeeeeeeee")
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64':uidb64, 'token':token})
            
            send_to = form.cleaned_data['email']
            email_subject = "Activate your acount"
            email_body = "Hi " + send_to[:6] + "Use this link to verify your account\n"+"http://"+domain+link
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@example.com',
                [send_to],
                )
            email.send(fail_silently=False)
            return HttpResponse("Verify Your Mail")
        else:
            print("invalidddddddddd")
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def activate(request, uidb64, token):
    try:
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # confirmation message then redirect to homepage
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
