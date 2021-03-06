from django.contrib.auth.backends import ModelBackend
from .models import User
import re
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
    }


class MutilLoginRequest(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('**************************MutilLogin***********************************')
        user_name = re.compile(r'^[a-zA-Z_]{6,}$')
        email_name = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
        phone_name = re.compile(r'^[0-9]{1,11}$')
        phone_res = re.match(phone_name, username)
        email_res = re.match(email_name, username)
        user_res = re.match(user_name, username)
        if user_res:
            print('user',user_res)
            user = User.objects.get(username=user_res.group(0))
        elif phone_res:
            print('phone',phone_res.group(0))
            user = User.objects.get(phone=phone_res.group(0))
        elif email_res:
            print('email',email_res)
            user = User.objects.get(email=email_res.group(0))
        else:
            print('error')
        # print(user)

        return user
        # pass
# class ModelBackend(object):
#     """
#     Authenticates against settings.AUTH_USER_MODEL.
#     """
#
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             user = UserModel._default_manager.get_by_natural_key(username)
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
#
#     def user_can_authenticate(self, user):
#         """
#         Reject users with is_active=False. Custom user models that don't have
#         that attribute are allowed.
#         """
#         is_active = getattr(user, 'is_active', None)
#         return is_active or is_active is None
#
#     def _get_user_permissions(self, user_obj):
#         return user_obj.user_permissions.all()
#
#     def _get_group_permissions(self, user_obj):
#         user_groups_field = get_user_model()._meta.get_field('groups')
#         user_groups_query = 'group__%s' % user_groups_field.related_query_name()
#         return Permission.objects.filter(**{user_groups_query: user_obj})
#
#     def _get_permissions(self, user_obj, obj, from_name):
#         """
#         Returns the permissions of `user_obj` from `from_name`. `from_name` can
#         be either "group" or "user" to return permissions from
#         `_get_group_permissions` or `_get_user_permissions` respectively.
#         """
#         if not user_obj.is_active or user_obj.is_anonymous or obj is not None:
#             return set()
#
#         perm_cache_name = '_%s_perm_cache' % from_name
#         if not hasattr(user_obj, perm_cache_name):
#             if user_obj.is_superuser:
#                 perms = Permission.objects.all()
#             else:
#                 perms = getattr(self, '_get_%s_permissions' % from_name)(user_obj)
#             perms = perms.values_list('content_type__app_label', 'codename').order_by()
#             setattr(user_obj, perm_cache_name, set("%s.%s" % (ct, name) for ct, name in perms))
#         return getattr(user_obj, perm_cache_name)
#
#     def get_user_permissions(self, user_obj, obj=None):
#         """
#         Returns a set of permission strings the user `user_obj` has from their
#         `user_permissions`.
#         """
#         return self._get_permissions(user_obj, obj, 'user')
#
#     def get_group_permissions(self, user_obj, obj=None):
#         """
#         Returns a set of permission strings the user `user_obj` has from the
#         groups they belong.
#         """
#         return self._get_permissions(user_obj, obj, 'group')
#
#     def get_all_permissions(self, user_obj, obj=None):
#         if not user_obj.is_active or user_obj.is_anonymous or obj is not None:
#             return set()
#         if not hasattr(user_obj, '_perm_cache'):
#             user_obj._perm_cache = self.get_user_permissions(user_obj)
#             user_obj._perm_cache.update(self.get_group_permissions(user_obj))
#         return user_obj._perm_cache
#
#     def has_perm(self, user_obj, perm, obj=None):
#         if not user_obj.is_active:
#             return False
#         return perm in self.get_all_permissions(user_obj, obj)
#
#     def has_module_perms(self, user_obj, app_label):
#         """
#         Returns True if user_obj has any permissions in the given app_label.
#         """
#         if not user_obj.is_active:
#             return False
#         for perm in self.get_all_permissions(user_obj):
#             if perm[:perm.index('.')] == app_label:
#                 return True
#         return False
#
#     def get_user(self, user_id):
#         try:
#             user = UserModel._default_manager.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None
#         return user if self.user_can_authenticate(user) else None