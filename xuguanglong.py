# -*- coding: UTF-8 -*-

def GBK(str):
    return str.decode('utf-8').encode('gbk')

print GBK("请输入内容：")