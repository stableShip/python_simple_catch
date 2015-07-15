# coding=utf-8
__author__ = 'JIE'
import time


class Catch():
    __catchMap = {}

    @classmethod
    def set(cls, key, value, expire):
        """
        :param key: 键
        :param value:值
        :param expire:过期时间
        :return:None
        """
        cls.__catchMap[key] = [value, time.time(), expire]

    @classmethod
    def get(cls, key):
        """
        :param key:键
        :return:值
        """
        arr = cls.__catchMap.get(key)
        if arr is not None:
            if time.time() - (arr[1] + arr[2]) <= 0:
                return arr[0]
            else:
                cls.__catchMap.pop(key)
        return None


