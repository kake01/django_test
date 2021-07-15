from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Message
from .forms import  MessageForm
from django.shortcuts import redirect


class MessageView(TemplateView):
    def __init__(self):
        self.params = {
        }

    def get(self, request):
        data = Message.objects.all()
        self.params = {
            'data': data,
            'form' : MessageForm(),
        }
        return render(request, 'chat/index.html', self.params)

    def post(self, request):
        #DBに保存
        obj = Message()
        # ユーザーDB作成したら外部キーに設定(TODO)
        # obj.owner_id = request.user.id
        # 返答は学習モデルを使用して作成(TODO)
        obj.respond = self.bot_respond(request.POST['content'])
        form = MessageForm(request.POST, instance=obj)
        form.save()
        return redirect(to="/chat")
    
    # バックエンドメソッドを読み込み返答を作成(TODO)
    def bot_respond(self, msg):
        return '貴方は言いました。「' + msg + '」と。'
