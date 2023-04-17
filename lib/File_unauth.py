# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/12 5:19 PM
@Auth ： xinghe
@File ：File_unauth.py
@IDE ：PyCharm
@Motto:但行好事，莫问前程
"""

from urllib3.exceptions import InsecureRequestWarning
from queue import Queue
import threading
from lib.Findjslink import FindInfo
from lib.url_unauth import Unauth_process
from run import MyClass
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ZooSpaider(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            domain = self._queue.get()
            try:
                self.spider(domain)
            except Exception as e:
                pass

    def spider(self, domain):
        try:
            main(domain)
        except Exception as e:
            pass

def main(user_input_url):
    my_finder = FindInfo()
    # 调用 Request_Js 方法，并传入一个 URL 参数
    data1, data2 = my_finder.Request_Js(user_input_url)
    # 从Path_Screen函数返回的js列表中深入递归提取path
    path_list_tmp = my_finder.While_Requests_Js(data2, user_input_url)
    # 保存最终提取的path，并去重，除去开头小数点
    path = []
    p_temp = []
    path.extend(data1)
    path.extend(path_list_tmp)
    path = list(set(path))
    for p_t in path:
        p_temp.append(p_t)
    for p in p_temp:
        if p.split("/")[0] == '.':
            p_re = p.replace(".", "")
            if p in path:
                path.remove(p)
            if p_re not in path:
                path.append(p_re)
    unauth = Unauth_process()
    unauth.geturl(user_input_url, path)

def file_thread(file_url):
    queue = Queue(maxsize=15000)
    for i in open(file_url, 'r+'):
        queue.put(i.replace('\n', ''))

    thread = []
    thread_count = 200

    for i in range(thread_count):
        thread.append(ZooSpaider(queue))
    for t in thread:
        t.start()
    for t in thread:
        t.join()
