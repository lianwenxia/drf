from celery import task
from django.core.mail import send_mail
import time


@task
def send_email_celery(to_email, trans):
    subject = '尚惠有品'
    message = ''
    from_email = 'shanghui<1213284679@qq.com>'
    recipient_list = ['1213284679@qq.com']
    html_message = '<p><a href="http://127.0.0.1:8000/users/active/'+trans+'">点击这里激活账号</a></p>'
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
              html_message=html_message)
    time.sleep(100)
