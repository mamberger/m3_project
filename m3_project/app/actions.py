from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    can_delete = True

    columns = [
        {
            'data_index': '__unicode__',
            'header': u'username',
        },
        {
            'data_index': 'email',
            'header': u'email',
        },
    ]


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    can_delete = True


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    can_delete = True