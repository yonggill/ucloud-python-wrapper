# -*- coding:utf-8 -*-


class NotAuthorized(Exception):
    """
    status code 401
    """
    def __str__(self):
        return u"Not Authorized. Account Token has problem."


class NoContainer(Exception):
    """
    status code 404
    """
    def __str__(self):
        return u"container does not exist."


class NoPermission(Exception):
    """
    status code 403
    """
    def __str__(self):
        return u"Ip or Account has no permission for target container."


class CanNotDelete(Exception):
    """
    status code 409
    """
    def __str__(self):
        return u"Object has child object. " \
               u"You can not do this Deletion. " \
               u"Delete child object first."


class ContentLengthOver(Exception):
    """
    status code 411
    """
    def __str__(self):
        return u"object to upload has over content length for normal upload " \
               u"or object data not serve for storage server. " \
               u"check your file system."