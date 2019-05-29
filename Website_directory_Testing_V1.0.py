# -*- coding:utf-8 -*-
#------------------------

# Author：秋某人的傻逼

#------------------------

#-----------构建思路-----------
#1.使用调用函数方式实现目录检测(由于市场上基本都是php源码，所以暂时不添加java源码，如果需要请自己手工添加)
#2.函数 easy_path : 包含常用后台目录Admin/admin/Login/login/manage/system/myadmin/administrator/administrators/Admin\/login，可以自定义简单后台关键词，即更改根目录下的easy_path.txt
#3.函数 frame_path : 包含常用框架目录 thinkphp，Yii，laravel，CodeIgniter，Zend Framework，CakePHP，Symfony，可以自定义框架目录，只需要将框架源码加入到source_path即可
#4.函数 dir_path : 包含从外部引入的字典，比如御剑1.5 加强字典版本，输入字典路径即可读取字典内容
#-----------构建思路-----------
import requests
import os
import re
import time
from Website_directory_Testing_2 import wbtesting

print ('[info]:--------------------|++++++++++++++++++++++|----------------')
print ('[info]:--------------++++++|---单个软件版本V1.0-------|++++++------')
print ('[info]:--------------------|++++++++++++++++++++++|----------------')
print ('[info]:--------------------|+++++++++++++++++++++++++++++++++++++|----------------')
print ('[info]:---------------+++++|---作者：秋某人的傻逼[熊猫爱皮卡丘]--|++++++------')
print ('[info]:--------------------|+++++++++++++++++++++++++++++++++++++|----------------')

#--------------------//----------
#函数部分
#--------------------//----------
def easy_path(target_url):
    print ('[info]:常用目录猜测开始...')
    for i in open('easy_path.txt','r'):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            response = requests.get(target_url+i, headers=headers)
            res_content = response.content
            pattern = r'很抱歉，您要访问的页面不存在！'
            pattern2 = r'页面找不到了'
            pattern3 = r'未找到页面'
            pattern4 = r'404.0 - Not Found'
            pattern5 = r'您访问的页面不存在!'
            search_one = re.search(pattern,res_content.decode('gbk'),re.M|re.I)
            search_two = re.search(pattern2, res_content.decode('gbk'), re.M | re.I)
            search_three = re.search(pattern3, res_content.decode('gbk'), re.M | re.I)
            search_four = re.search(pattern4, res_content.decode('gbk'), re.M | re.I)
            search_five = re.search(pattern5, res_content.decode('gbk'), re.M | re.I)
            if search_one or search_two or search_three or search_four or search_five or response.status_code == 404  or response.status_code == 400:
                print ('[payload]:', i.strip('\n'), '|', '[info]:404页面已被筛选掉！')
            else:
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：',response.status_code)
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：', response.status_code, file=open('result.txt','a+'))
        except Exception as e:
            print(e)
            continue
def frame_path(target_url):
    print ('[info]:框架目录检测开始...')
    # 定义要获取的父目录
    dirname = '.'
    # 获取目录中子目录和文件
    paths = os.walk(dirname)
    # 迭代生成结果
    rets = []
    for parent, directories, files in paths:
        for d in directories:
            rets.append(os.path.join(parent, d))
        for f in files:
            rets.append(os.path.join(parent, f))
    # 整理路径
    rets = [r[len(dirname) + 1:] for r in rets]
    rets = [r.replace('\\', '/') for r in rets]
    # 输出到文件
    with open('dir_test.txt', 'w') as f:
        f.write('\n'.join(rets))
        f.close()
    for i in open('dir_test.txt','r'):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            response = requests.get(target_url+ '/' + i, headers=headers)
            res_content = response.content
            pattern = r'很抱歉，您要访问的页面不存在！'
            pattern2 = r'页面找不到了'
            pattern3 = r'未找到页面'
            pattern4 = r'404.0 - Not Found'
            pattern5 = r'您访问的页面不存在!'
            search_one = re.search(pattern,res_content.decode('gbk'),re.M|re.I)
            search_two = re.search(pattern2, res_content.decode('gbk'), re.M | re.I)
            search_three = re.search(pattern3, res_content.decode('gbk'), re.M | re.I)
            search_four = re.search(pattern4, res_content.decode('gbk'), re.M | re.I)
            search_five = re.search(pattern5, res_content.decode('gbk'), re.M | re.I)
            if search_one or search_two or search_three or search_four or search_five or response.status_code == 404  or response.status_code == 400:
                print ('[payload]:', i.strip('\n'), '|', '[info]:404页面已被筛选掉！')
            else:
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：',response.status_code)
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：', response.status_code, file=open('result.txt','a+'))
        except Exception as e:
            print(e)
            continue
def dir_path(target_url):
    target_dir = input('请输入字典的绝对路径！例如：F:\\\\document\\\项目\\\\测试代码\\source\\\\dir_test.txt：')
    for i in open(target_dir,'r',encoding='gbk'):
        try:
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            response = requests.get(target_url+i, headers=headers)
            res_content = response.content
            pattern = r'很抱歉，您要访问的页面不存在！'
            pattern2 = r'页面找不到了'
            pattern3 = r'未找到页面'
            pattern4 = r'404.0 - Not Found'
            pattern5 = r'您访问的页面不存在!'
            search_one = re.search(pattern,res_content.decode('gbk'),re.M|re.I)
            search_two = re.search(pattern2, res_content.decode('gbk'), re.M | re.I)
            search_three = re.search(pattern3, res_content.decode('gbk'), re.M | re.I)
            search_four = re.search(pattern4, res_content.decode('gbk'), re.M | re.I)
            search_five = re.search(pattern5, res_content.decode('gbk'), re.M | re.I)
            if search_one or search_two or search_three or search_four or search_five or response.status_code == 404  or response.status_code == 400:
                print ('[payload]:', i.strip('\n'), '|', '[info]:404页面已被筛选掉！')
            else:
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：',response.status_code)
                print('[payload]:', i.strip('\n'), '|', '网址返回包长度是：', len(response.content), '|', '网站返回状态码是：', response.status_code, file=open('result.txt','a+'))
        except Exception as e:
            print(e)
            continue
#--------------------//----------
#判断功能部分
#--------------------//----------
target_url_judge = input('请选择您要进行的测试模式： 1 OR 2 -----+>>批量请按1，单个url请按2:')
if int(target_url_judge) == 1:
    urls_path = input('请输入采集好的网址的路径,例如：C:\\\\Users\\\\admin90\\\\Documents\\\\WeChat Files：')
    for target_url in open(urls_path , 'r'):
        wbtesting.easy_path(target_url)
        wbtesting.frame_path(target_url)
        wbtesting.dir_path(target_url)
    print ('检测完毕...等待20000秒结束...')
    time.sleep(20000)
elif int(target_url_judge) == 2:
    target_url = input('请输入url地址，例如：http://www.baidu.com:')
    easy_path(target_url)
    frame_path_input = input('请问是否要进行框架目录检测模式？ 1 OR 2  -----+>>>是请按1，不是请按2：')
    if int(frame_path_input) == 1:
        frame_path(target_url)
    elif int(frame_path_input) == 2:
        print ('已经取消框架目录检测...')
    else:
        print ('您的输入有误,程序结束！')
        exit()
    dir_path_input = input('请问是否要进行外部调用目录检测模式？ 1 OR 2  -----+>>>是请按1，不是请按2：')
    if int(dir_path_input) == 1:
        dir_path(target_url)
    elif int(dir_path_input) == 2:
        print ('已经取消框架目录检测...')
    else:
        print ('您的输入有误,程序结束！')
        exit()
else:
    print ('您输入有误,程序结束!')
    exit()

if '__name__' == '__main__':
    print ('调用模块成功...')