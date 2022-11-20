from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

# Create your views here.

# 登录界面
from vsasApp import models
import json
import pandas as pd

f = open('./data/json_data.json')
json_data = json.load(f)
f.close()


def login(request):
    if request.method == 'POST':
        # 获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # 验证信息（这里写固定，用户：admin 密码：admin）
        # 后期可以使用数据库和加密手段进一步完善
        if (username == 'admin') & (password == 'admin'):
            # 验证通过
            return redirect(reverse('index', kwargs={'username': username, 'where': 'DashBoard'}))
        else:
            return render(request, "vsasLogin.html", {
                'errMsg_username': '请仔细检查用户名',
                'errMsg_password': '请仔细检查密码'
            })

    return render(request, "vsasLogin.html")


# 主界面
def index(request, username, where):
    print(username, where)
    # 查找项目
    projects = models.UserProject.objects.filter(username=username)
    tables = models.UserTable.objects.filter(username=username)
    return render(request, 'index.html', {
        'username': username,
        'where': where,
        'projects': projects,
        'tables': tables,
        'project_name': None,
        'table_name': None
    })


# 项目展示（数据都往这里传递吧）
def projectShow(request, username, project_name):
    # print(json_data)
    return render(request, 'index.html', {
        'username': username,
        'where': 'Project',
        'project_name': project_name,
        'table_name': None,
        'json_data': json_data
    })


# 展示表
def tableShow(request, username, table_name):
    table_path = models.UserTable.objects.filter(username=username).filter(table_name=table_name).values_list(
        'table_path')
    table_data = []
    table_df = pd.read_csv(table_path[0][0]).head(50).reset_index()  # 只显示50行
    table_data.append(list(table_df.columns))
    for i in range(50):
        table_data.append(list(table_df.iloc[i]))
    print(table_data)
    return render(request, 'index.html', {
        'username': username,
        'where': 'Table',
        'project_name': None,
        'table_name': table_name,
        'table_data': table_data
    })


# 测试Echars
def testEcharts(request):
    return render(request, "testEcharts.html")
