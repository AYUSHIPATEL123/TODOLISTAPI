from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User


try:
    @shared_task
    def send_email(user_id):
    # print("hellooo,.....")
        user = User.objects.get(pk=user_id)
        subject = "your account has been created 👍successfully"
        message = f"🙋🏼 welcome {user.first_name} {user.last_name} to \n our To-Do-List-API webapp "
        send_email_massege = EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=[user.email])
        send_email_massege.send(fail_silently=False)
        return None  
except Exception as e:
    print("error occured",e)
