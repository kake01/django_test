from django.test import TestCase
from django.urls import reverse, resolve

from .views import TodoView

class TODOTest(TestCase):
    """chat ページへのURLでアクセスする時のリダイレクトをテスト"""
    def test_post_index_url(self):
        url = '/todo/'# urlの値が入る
        view = resolve(url)
        self.assertEqual(view.func.view_class, TodoView)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.get(reverse('todo'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
        response = self.client.post(reverse('todo'))
        self.assertEqual(response.status_code, 200)