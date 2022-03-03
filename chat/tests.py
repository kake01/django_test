from django.test import TestCase
from django.urls import reverse, resolve

from .models import Message
from .views import MessageView


# class MessageModelTests(TestCase):
    # User(ログインIDを設定しないとダメみたい)
    # def test_is_empty(self):
    #     # 初期状態では空である確認
    #     saveed_messages = Message.objects.all()
    #     self.assertEqual(saveed_messages.count(), 0)

    # def test_is_count_one(self):
    #     # 1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト
    #     message = Message(owner='ikumakakeru',content='送信メッセージ', respond='返答メッセージ')
    #     message.save()
    #     saved_messages = Message.objects.all()
    #     self.assertEqual(saved_messages.count(), 1)

class ChatTest(TestCase):
    """chat ページへのURLでアクセスする時のリダイレクトをテスト"""
    def test_post_index_url(self):
        url = '/chat/'# urlの値が入る
        view = resolve(url)
        self.assertEqual(view.func.view_class, MessageView)

    def test_get(self):
        """GET メソッドでアクセスしてステータスコード302を返されることを確認"""
        # LoginRequiredMixinの関係でリダイレクトされる
        response = self.client.get(reverse('chat_bot_message'))
        self.assertEqual(response.status_code, 302)

