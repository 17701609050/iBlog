# -*- coding: utf-8 -*-
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail


def send_verify_email(recipients, verify_url):
    """
    发送验证邮箱邮件
    :param to_email: 收件人邮箱
    :param verify_url: 验证链接
    :return: None
    """
    recipient_list = []
    cc = [settings.ROBOT_ACCOUNT_EMAIL]
    if isinstance(recipients, list):
        recipient_list = recipients[:]
    else:
        recipient_list.append(recipients)

    subject = "iBlog 邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用iBlog。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (recipient_list, verify_url, verify_url)
    try:
        messages = []
        for recipient in recipient_list:
            msg = mail.EmailMessage(subject=subject, body=html_message, to=recipient_list, cc=cc)
            msg.content_subtype = "html"
            messages.append(msg)

        connection = mail.get_connection(fail_silently=settings.DEBUG)
        connection.send_messages(messages)
        if msg.send():
            print('******************send ok*********************')
    except Exception as e:
        print(str(e))
        print('******************send fail*********************')
