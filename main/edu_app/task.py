from celery import shared_task

from django.core.mail import EmailMessage


@shared_task
def send_course_email(student_name, course_name, student_email, date):
    mail_subject = "Регистрация на курс завершена"
    message = f" {student_name}, вы записались на курс {course_name} спасибо вам большое!\n Занятия начнуться {date}.\n С уважением IT-world."
    email = EmailMessage(mail_subject, message, to=[student_email])
    email.send()