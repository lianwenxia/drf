from rest_framework import serializers
from django_redis import get_redis_connection
from .models import User
from celery import Celery
from shanghuishop.settings.dev import SECRET_KEY
import re
from shanghuishop.task import send_email_celery
from itsdangerous import TimedJSONWebSignatureSerializer as TJS, SignatureExpired
from rest_framework_jwt.settings import api_settings


'''用户注册验证与创造'''
class UserSerialize(serializers.ModelSerializer):
    # token = serializers.CharField(label='JWT token', read_only=True)
    password_confirm = serializers.CharField(label='确认密码', write_only=True)
    phone_msg = serializers.CharField(label='短信验证码', write_only=True)

    class Meta:
        model = User
        # fields = ('username', 'phone', 'password', 'password_confirm', 'phone_msg', 'email', 'token')
        fields = ('username', 'phone', 'password', 'password_confirm', 'phone_msg', 'email')

    def validate(self, data):
        print('**********************validate*************************')
        # print(data['phone'])
        # con = get_redis_connection()
        # true_phone = data['phone']
        # true_msg = con.get(true_phone)

        # if data['password'] != data['password_confirm']:
        #     raise serializers.ValidationError('两次输入的密码不一致!')
        # elif len(data['password']) < 6:
        #     raise serializers.ValidationError('输入的密码不小于6位!')
        # elif len(data['username']) < 6:
        #     raise serializers.ValidationError('输入的用户名不小于6位!')
        # elif not true_msg:
        #     raise serializers.ValidationError('短信验证码不存在!')
        # elif true_msg.decode() != data['phone_msg']:
        #     raise serializers.ValidationError('短信验证码错误!')
        return data

    def create(self, validate_data):
        print('**********************create*************************')
        print(validate_data)
        del validate_data['password_confirm']
        del validate_data['phone_msg']
        user = User.objects.create_user(**validate_data)
        # user.is_active = 0
        # user.save()
        # email = validate_data['email']
        # username = validate_data['username']
        # ts = TJS(SECRET_KEY, 3600)
        # trans = ts.dumps(username).decode()
        # send_email_celery.delay(to_email=email, trans=trans)
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(user)
        # token = jwt_encode_handler(payload)
        # user.token = token
        return user


'''用户中心信息的显示与修改'''


class UserInfoSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'first_name', 'fixtel', 'qq', 'birth')

    def update(self, instance, validated_data):
        print('******************************in_change*****************************')
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.fixtel = validated_data.get('fixtel', instance.fixtel)
        instance.qq = validated_data.get('qq', instance.qq)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.birth = validated_data.get('birth', instance.birth)
        instance.save()
        return instance
from rest_framework.permissions import IsAuthenticated