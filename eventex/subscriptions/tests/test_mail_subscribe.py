from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Felipe Fontes', cpf='12345678901',
                    email='iffontes9@gmail.com', phone='21-99955-4804')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect =  'iffontes9@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_emial_to(self):
        expect = ['iffontes9@gmail.com', 'iffontes9@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

            contents = ['Felipe Fontes',
                        '12345678901',
                        'iffontes9@gmail.com',
                        '21-99955-4804']
            for content in contents:
                with self.subTest():
                    self.assertIn(content, self.email.body)
