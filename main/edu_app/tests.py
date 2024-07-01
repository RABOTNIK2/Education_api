from django.test import TestCase
from .models import *
from django.urls import reverse
from urllib.parse import urlencode

class EducationsTets(TestCase):
    def setUp(self):
        self.course = Courses.objects.create(
            name = 'курсы по чесанию яиц',
            start_date = '2023-07-07',
            duration = 60,
            ruler = "Хуй с горы",
            descriptin = "gdgdregge"
        )
        self.data = {'email': 'sspredovich@mail.ru', 'first_name': 'Stolb', 'last_name': 'Potstolbnik', 'password': 'shiiish228'}
        self.student = Student.objects.create_user(**self.data)
    
    def test_courselist(self):
        response = self.client.get(reverse("courses-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.course.start_date, response.content.decode())

    def test_course_create(self):
        data = {'name': 'fkjdkjhjdg','start_date': '2000-04-04', 'duration': 35, 'ruler': 'ppfdf', 'descriptin': 'ffdgdhd'}
        response = self.client.post(reverse("courses-list"), data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('fkjdkjhjdg', response.content.decode())

    def test_course_detail(self):
        data = urlencode({'name': 'dfgdgdg', 'start_date': self.course.start_date, 'duration': self.course.duration, 'ruler': self.course.ruler, 'descriptin': self.course.descriptin})
        response = self.client.put(reverse("courses-detail", kwargs={'pk': self.course.pk}), data, content_type="application/x-www-form-urlencoded")
        updated_course = Courses.objects.get(pk = self.course.pk)
        self.assertEqual(updated_course.name, 'dfgdgdg')

    def test_student(self):
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.student.email, response.content.decode())

# Create your tests here.
