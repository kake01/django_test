from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Message
from .forms import  MessageForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class MessageView(LoginRequiredMixin, TemplateView):
    def __init__(self):
        self.params = {
        }
    
    def get(self, request):
        data = Message.objects.all()
        self.params = {
            'data': data,
            'form' : MessageForm(),
        }
        return render(request, 'chat/chat.html', self.params)

    def post(self, request):
        #DBに保存
        obj = Message()
        # TODO ユーザーDB作成したら外部キーに設定
        obj.owner_id = request.user.id
        obj.respond = self.bot_respond(request.POST['content'])
        form = MessageForm(request.POST, instance=obj)
        form.save()

        data = Message.objects.filter(owner_id=request.user.id)

        # TODO wavファイルの書き換え処理
        return redirect(to="/chat")
    
    # バックエンドメソッドを読み込み返答を作成(TODO)
    def bot_respond(self, msg):
        return '貴方は言いました。「' + msg + '」と。'
