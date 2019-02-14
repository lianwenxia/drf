from rest_framework import serializers
from django_redis import get_redis_connection


class MsgCodeSerialize(serializers.Serializer):

    uuid = serializers.UUIDField()
    rand_str = serializers.CharField(max_length=4, min_length=4)

    def validate(self, data):
        print(data)
        uuid = str(data['uuid'])
        rand_str = data['rand_str']
        rand_str = rand_str.upper()
        con = get_redis_connection()
        img_str = con.get(uuid)
        print('#' * 80)
        print(self.context['view'].kwargs['phone'])
        if not img_str:
            # print('#' * 80)
            # print('验证码不存在')
            raise serializers.ValidationError('验证码不存在')
        elif rand_str == img_str.decode():
            con.delete(uuid)
            print('#'*80)
            print('验证通过')
        else:
            # print('#'*80)
            # print('验证失败')
            raise serializers.ValidationError('验证失败')

        return data