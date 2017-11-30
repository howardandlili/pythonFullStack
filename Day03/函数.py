#!/user/bin/env python
# __author__ = 'Howie'
# date : 2017/11/30


def information(gender="man", *args, **kwargs):
    print(
        '''
        name:%s
        age:%d
        job:%s
        sal:%d
        address:%s
        gender:%s
        ''' % (kwargs["name"], args[0], kwargs["job"], args[1], kwargs["address"], gender)
    )


information("female", 30, 12000, name="hy", job="IT", address="GZ")
