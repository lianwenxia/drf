from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserSerialize, UserInfoSerialize
from .models import User
from django.contrib import auth
import json
from shanghuishop.settings.dev import SECRET_KEY
from itsdangerous import TimedJSONWebSignatureSerializer as TJS
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserView(CreateAPIView):

    serializer_class = UserSerialize


class UserInfoView(RetrieveAPIView):

    serializer_class = UserInfoSerialize

    permission_classes = (IsAuthenticated,)

    def get_object(self):
        print('************************userinfo******************************')
        print(self.request.user)
        return self.request.user


class LoginView(View):
    def post(self, request):
        print('***************************user*************************************')
        res = request.body.decode()
        user_list = json.loads(res)
        pwd = user_list['password']
        username = user_list['username']
        user = auth.authenticate(username=username, password=pwd)
        print(user)
        if not user:
            print('user does not exit')
        else:
            auth.login(request=request, user=user)
            response = JsonResponse('ok', safe=False)
            response.set_cookie('user', username)
            return response
            # return JsonResponse('ok', safe=False)

        return HttpResponse('fine')


class ActiveView(View):

    def get(self, request, userinfo):
        ts = TJS(SECRET_KEY, 3600)
        trans = ts.loads(userinfo)
        user = User.objects.get(username=trans)
        user.is_active = 1
        user.save()
        return HttpResponse('激活成功')


class ChangeView(APIView):
    # serializer_class = UserSerialize
    # queryset = User.objects.get(id=21)
    # def get(self,request):
    # return JsonResponse('get',safe=False)

    def post(self,request):
        id=request.data['id']
        user = User.objects.get(id=id)
        print('****************change_text********************')
        print(request.data['id'])
        del request.data['id']
        print(request.data)
        serializer = UserInfoSerialize().update(user, request.data)
        # serializer.is_valid(raise_exception=True)
        # print(serializer)
        print(request.data.get('username'))
        return JsonResponse('ok', safe=False)


