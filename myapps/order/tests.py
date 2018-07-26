from django.test import TestCase, override_settings, Client
import requests

from art.models import Art
from art.utils import rds

# Create your tests here.
class ArtTestCase(TestCase):
    def test_show(self):
        client = Client(enforce_csrf_checks=False)
        resp = client.get('http://127.0.0.1:8000/art/show/1/')
        self.assertEqual(resp.status_code, 200)

    def test_redis(self):
        print('--单元测试 redis--')
        self.assertEqual(rds.exists('artTop'), True)

    @override_settings(DEBUG=False)
    def test_art_list(self):
        print('－－测试Art数据模型－－')
        Art.objects.create(title='haa')
        Art.objects.create(title='ha223a')
        Art.objects.create(title='hah33a')
        artQS = Art.objects.all()
        print(artQS)
        self.assertGreater(artQS.count(), 2, '没有大于3')
        print(artQS.values())
