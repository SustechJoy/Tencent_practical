# -*- coding: utf-8 -*-
"""

@project: Tencent
@author: yi
@e-mail: 11612917@mail.sustc.edu.cn
@file: get_repository.py
@time: 11/26/18 9:15 AM
"""

import requests
import json
import time


class RepositoryGET:
    def __init__(self, search_id, name="", secrect=""):
        self.file_name = 'full_name.txt'
        self.search_id = search_id
        self.repo_num = 0
        self.name = ""
        self.secret = ""
        self.sleep_time = 6
        if name != "":
            self.name = name
            self.secret = secrect
            self.sleep_time = 1

    def search(self):
        full_name_file = open(self.file_name, 'w')
        page_num = 1
        while True:
            if self.name == "":
                url = 'https://api.github.com/search/repositories?q=%s&page=%d' % (self.search_id, page_num)
            else:
                url = 'https://api.github.com/search/repositories?q=%s&page=%d' % (self.search_id, page_num) \
                      + "&client_id=%s&client_secret=%s" % (self.name, self.secret)
            req = requests.get(url)
            if str(req) == '<Response [422]>':
                print("----已得到所有仓库名称----")
                print("----接下来将获取issue----")
                break
            elif str(req) == '<Response [403]>':
                print('----ip使用已超出最大限制----')
                print('----可使用ip池进行访问优化----')
                print('----请稍等----')
                self.sleep_time = 6
                time.sleep(self.sleep_time)
            elif not req.json()["items"]:
                print("----已得到所有仓库名称----")
                print("----接下来将获取issue----")
                break
            else:
                print("----正在获取仓库信息,当前处于第%d页----" % page_num)
                print('----请稍等----')
                JSON = req.json()
                json.dumps(JSON, indent=2)
                for j in JSON['items']:
                    name = j['full_name']
                    full_name_file.write(name + '\n')
                    self.repo_num += 1
                page_num += 1
                time.sleep(self.sleep_time)
        full_name_file.close()
