# -*- coding: utf-8 -*-
"""

@project: Tencent
@author: yi
@e-mail: 11612917@mail.sustc.edu.cn
@file: main.py
@time: 11/26/18 9:15 AM
"""

from get_repository import RepositoryGET
from get_issue import IssueGET
import getpass


def search(name, secret):
    repo = RepositoryGET(search_id, name, secret)
    repo.search()
    issue = IssueGET(repo.repo_num, name, secret)
    issue.search()


if __name__ == '__main__':
    choice = input("请选择是否登录github账号,以得到给定时间内更多访问次数:\n 1:登录\n 2:不登录\n")
    name = secret = ""
    if int(choice) == 1:
        name = input("请输入github用户名:")
        secret = getpass.getpass("请输入github密码:")
    search_id = input("请输入要搜索的关键字: ")
    search(name, secret)
