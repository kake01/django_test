from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Message
from .forms import  MessageForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class MessageView(TemplateView):
    def __init__(self):
        self.params = {
        }
    
    # @login_required
    def get(self, request):
        data = Message.objects.all()
        self.params = {
            'data': data,
            'form' : MessageForm(),
        }
        return render(request, 'chat/index.html', self.params)

    @login_required
    def post(self, request):
        #DBに保存
        obj = Message()
        # TODO ユーザーDB作成したら外部キーに設定
        # obj.owner_id = request.user.id
        # TODO 返答は学習モデルを使用して作成
        obj.respond = self.bot_respond(request.POST['content'])
        form = MessageForm(request.POST, instance=obj)
        form.save()
        # TODO wavファイルの書き換え処理
        return redirect(to="/chat")
    
    # バックエンドメソッドを読み込み返答を作成(TODO)
    def bot_respond(self, msg):
        return '貴方は言いました。「' + msg + '」と。'
