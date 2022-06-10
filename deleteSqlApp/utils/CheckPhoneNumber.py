# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2022 - 06 -10
# @File: CheckPhoneNumber.py

import re
class CheckPhoneNumber:


    # 正则匹配手机号
    @staticmethod
    def check_phone_number(account:str):
        if len(account)<11:
            return "False" ,"请检查手机号格式"

        number = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', account)
        if number ==[]:
            return "False", "请检查手机号格式"
        else:
            return "True", number





