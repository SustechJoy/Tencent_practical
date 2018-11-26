# -*- coding: utf-8 -*-
"""

@project: Tencent
@author: yi
@e-mail: 11612917@mail.sustc.edu.cn
@file: get_issue.py
@time: 11/26/18 9:15 AM
"""

import requests
import time
import csv


class IssueGET:
    def __init__(self, repo_num, name="", secrect=""):
        self.in_name = 'full_name.txt'
        self.output = 'issue.csv'
        self.repo_num = repo_num
        self.name = ""
        self.secret = ""
        self.sleep_time = 6
        if name != "":
            self.name = name
            self.secret = secrect
            self.sleep_time = 1

    def search(self):
        with open(self.output, 'w', newline="") as file:
            csv_file = csv.writer(file)
            csv_header = ['full_name', 'repository_url', 'node_id', 'comments_url', 'number', 'title', 'state', 'body']
            csv_file.writerow(csv_header)
        with open(self.in_name, 'r') as file:
            i = 1
            for line in file.readlines():
                line = line[:-1]
                page_num = 1
                i += 1
                while True:
                    if self.name == "":
                        issue_url = 'https://api.github.com/repos/%s/issues?page=%d' % (line, page_num)
                    else:
                        issue_url = 'https://api.github.com/repos/%s/issues?page=%d' % (line, page_num) \
                                    + "&client_id=%s&client_secret=%s" % (self.name, self.secret)
                    issue_req = requests.get(issue_url)
                    time.sleep(self.sleep_time)
                    if not issue_req.json():
                        if i <= self.repo_num:
                            print("----已得到当前仓库所有issue信息,剩余条目:%d----" % (self.repo_num - i))
                        break
                    elif str(issue_req) == '<Response [403]>':
                        print('----ip使用已超出最大限制----')
                        print('----可使用ip池进行访问优化----')
                        print('----请稍等----')
                        self.sleep_time = 6
                    else:
                        print("----正在获取当前仓库issue信息----")
                        print('----请稍等----')
                        JSON = issue_req.json()
                        self.transfer(line, JSON)
                        page_num += 1

    def transfer(self, full_name, data):
        file = open(self.output, 'a+', newline="")
        csv_file = csv.writer(file)
        for item in data:
            data_needed = [full_name, item['repository_url'], item['node_id'], item['comments_url'],
                           item['number'], item['title'], item['state'], item['body']]
            csv_file.writerow(data_needed)
        file.close()
