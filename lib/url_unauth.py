# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/12 4:54 PM
@Auth ： xinghe
@File ：url_unauth.py
@IDE ：PyCharm
@Motto:但行好事，莫问前程
"""
import re
import requests
from lib.Findjslink import FindInfo

class Unauth_process:

    def __int__(self):
        super().__init__()

    def is_not_matched(self,string):
        regex = re.compile(
            r"\.(js|html|woff|ico|jpg|png|mp3|mp4|wasm)$|text\/(javascript|css)|static\/(css|js)|M/D/YYYY|!/|/\$|://|/?#|.woff?|/条/页|.ttf",
            re.IGNORECASE)
        return not bool(regex.search(string))

    def geturl(self,url, path):
        for i in path:
            if self.is_not_matched(str(i)):
                try:
                    result = requests.get(url=url + i, timeout=3, verify=False)
                    if result.status_code == 200 or result.status_code == 302 or result.status_code == 405:
                        if len(result.text) != 0 and 'html' not in result.text:
                            print(f"\033[1;32m[Success]\033[0m\033[1;31m\033[0m",
                                  f"\033[0;33m{result.url}\033[0m", f"\033[0;33m{result.status_code}\033[0m",
                                  f"\033[0;33m{len(result.text)}\033[0m", f"\033[1;32m{result.text}\033[0m")
                            with open('api.txt', 'a+') as f:
                                f.write('-' * 80 + '\n' + result.url + ' --- ' + str(len(result.text)) + '   ' + result.text + '\n')
                                f.close()
                except Exception as e:
                    pass
            elif '.js' in str(i):
                try:
                    result = requests.get(url=url + i, timeout=3, verify=False)
                    FindInfo.get_Secret(result)
                except Exception as e:
                    pass


