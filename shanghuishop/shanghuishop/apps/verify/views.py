from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse, JsonResponse
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
import random
from django_redis import get_redis_connection

from .serializers import MsgCodeSerialize

from shanghuishop.utils.yuntongxun.sms import CCP
# Create your views here.


class TestView(APIView):
    def get(self, request):
        print(request)
        return HttpResponse('api')

class ImgCodeView(View):
    def get(self, request, uuid):
        bgcolor = (random.randrange(20, 100), random.randrange(
            20, 100), 255)
        width = 100
        height = 25
        # 创建画面对象
        im = Image.new('RGB', (width, height), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)
        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, height))
            fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
            draw.point(xy, fill=fill)
        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
        font = ImageFont.truetype('FreeMono.ttf', 23)
        # 构造字体颜色
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        # 存入session，用于做进一步验证
        request.session['verifycode'] = rand_str
        # 内存文件操作
        buf = BytesIO()
        # 将图片保存在内存中，文件类型为png
        im.save(buf, 'png')
        print(rand_str)
        print(uuid)
        con = get_redis_connection()
        con.setex(name=uuid, time=3000, value=rand_str)
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(buf.getvalue(), 'image/png')

# class MsgCodeView(APIView):
#
#     def get(self, request, phone):
#         # self.get_serializer
#         # print(request.query_params)
#         # res = request.query_params['rand_str']
#         # print(res.upper())
#
#         # 校验验证码
#
#         # 127.0.0.1:8000/msg_code/{phone}/?uuid={uuid}&rand_str={rand_str}
#         serialize = MsgCodeSerialize(data=request.query_params)
#         serialize.is_valid(raise_exception=True)
#
#         # 发送短信
#         # print(phone)
#         alert = ''
#         con = get_redis_connection()
#         pipe_obj = con.pipeline()
#         # 若是手机验证码已过期或不存在
#         if not con.get(phone):
#             rand_num = random.randint(1000, 9999)
#             ccp = CCP()
#             ccp.send_template_sms(phone, [rand_num, 5], 1)
#             con.setex(name=phone, time=3000, value=rand_num)
#             pipe_obj.execute()
#             alert = '已发送'
#         # 若是手机验证码未过期
#         else:
#             # print('#'*80)
#             alert = '勿重复发送'
#         return JsonResponse({'alert': alert})

class MsgCodeView(GenericAPIView):

    serializer_class = MsgCodeSerialize

    def get(self, request, phone):
        # 通过get_serializer来创建serializer对象的时候会补充context,context包括request,format和view
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # 校验验证码
        # 127.0.0.1:8000/msg_code/{phone}/?uuid={uuid}&rand_str={rand_str}

        # serialize = MsgCodeSerialize(data=request.query_params)
        # serialize.is_valid(raise_exception=True)

        # 发送短信
        # print(phone)
        # alert = ''
        # con = get_redis_connection()
        # # pipe_obj = con.pipeline()
        # # 若是手机验证码已过期或不存在
        # if not con.get(phone):
        #     rand_num = random.randint(1000, 9999)
        #     ccp = CCP()
        #     ccp.send_template_sms(phone, [rand_num, 5], 1)
        #     con.setex(name=phone, time=3000, value=rand_num)
        #     pipe_obj.execute()
        #     alert = '已发送'
        # # 若是手机验证码未过期
        # else:
        #     # print('#'*80)
        #     alert = '勿重复发送'
        # return JsonResponse({'alert': alert})
        return HttpResponse('ok')




