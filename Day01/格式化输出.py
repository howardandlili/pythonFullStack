#!/user/bin/env python
#__author__ = 'Howie'
#date : 2017/11/25

name = input("name:")
age = input("age:")
job = input("job:")
sal = input("sal:")

if age.isdigit(): #判断能不能转成整数
    age=int(age)
if sal.isdigit():
    sal=int(sal)


exit(
'''
-------info of %s--------
name:%s
age:%s
job:%s
sal:%s
brand:%s
-------end--------
'''%(name,name,age,job,sal,(2017-age))
)