# -*- coding: utf-8 -*-
"""

@project: Tencent
@author: yi
@e-mail: 11612917@mail.sustc.edu.cn
@file: test.py
@time: 11/26/18 11:22 AM
"""

from github import Github, GithubException
import getpass
import csv

output = 'issue.csv'

if __name__ == '__main__':
    choice = input("请选择是否登录github账号,以得到给定时间内更多访问次数:\n 1:登录\n 2:不登录\n")
    name = secret = ""
    if int(choice) == 1:
        name = input("请输入github用户名:")
        secret = getpass.getpass("请输入github密码:")
    with open(output, "w", newline="") as file:
        csv_file = csv.writer(file)
        csv_header = ['full_name', 'comments_url', 'number', 'title', 'state', 'body']
        csv_file.writerow(csv_header)
    if name != "":
        g = Github(name, secret)
    else:
        g = Github()
    try:
        file = open(output, 'a+', newline="")
        csv_file = csv.writer(file)
        repos = g.search_repositories(query="go-back-n-udp")
        for repo in repos:
            for issue in repo.get_issues():
                print(issue.comments_url)
                data_needed = [repo.full_name,
                               issue.comments_url,
                               issue.number,
                               issue.title,
                               issue.state,
                               issue.body]
                csv_file.writerow(data_needed)

        file.close()
    except GithubException:
        print("----github api已达最大访问次数----")
        print("----请使用github账号登录以提高访问次数限制----")
        print("----如已登录,请检查用户名或密码,或稍后重试----")
        file.close()
