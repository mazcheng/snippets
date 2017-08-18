#!/apps/ns/python/bin/python
# _*_coding:utf-8_*_

"""
@author: mazhicheng
@file: so_login.py
@time: 2017/8/18 10:45

Log in to StackOverflow by selenium or Chrome
"""


from selenium import webdriver
import time

# reload browser core
driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs\bin\phantomjs.exe')
print 'begin', time.ctime()

# send requests
driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=http%3a%2f%2fstackoverflow.com%2fusers%2f6370293%2fzlxs23%3ftab%3dtopactivity")

time.sleep(20)

#获取用户名框并输入
elem = driver.find_element_by_xpath('//*[@id="email"]')
elem.send_keys("XXX")

#获取密码框并输入
elem = driver.find_element_by_xpath('//*[@id="password"]')
elem.send_keys("XXX")


# 通过id选择到登录键
driver.find_element_by_id('submit-button').click()


time.sleep(5)

#保存页面截图和源码
name = './' + time.ctime().replace(' ','-')+'.png'

driver.save_screenshot(name)

time.sleep(5)

print 'end',time.ctime()
driver.close()