from django.test import TestCase
from .models import Message


class MessageModelTests(TestCase):
    def test_is_empty(self):
        # 初期状態では空である確認
        saveed_messages = Message.objects.all()
        self.assertEqual(saveed_messages.count(), 0)

    def test_is_count_one(self):
        # 1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト
        message = Message(owner='ikumakakeru',content='送信メッセージ', respond='返答メッセージ')
        message.save()
        saved_messages = Message.objects.all()
        self.assertEqual(saved_messages.count(), 1)