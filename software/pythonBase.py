#-*- coding: UTF-8 -*-
import time
 
def foo():
    print 'in foo()'
 
# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
     
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
     
    # 将包装后的函数返回
    return wrapper
 
foo = timeit(foo)
foo()

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
 
@timeit
def foo():
    print 'in foo()'
 
foo()

import threading,queue
import time

# def consumer(n):
#     while True:
#         print("\033[32;1mconsumer [%s]\033[0m get task:  %s" % (n,q.get()))
#         time.sleep(1)
#         q.task_done()#每get一次包子，像其他进程告知队列信息
# def producer(n):
#     count = 1
#     while True:
#         #time.sleep(1)
#         #if q.qsize() <3:
#         print("prodcer [%s] produced a new task : %s" %(n,count))
#         q.put(count)
#         count +=1
#         q.join() #queue is emtpy # 等到队列为空在继续往下执行
#         print("all taks has been cosumed by consumers...")

# q = queue.Queue()
# c1 = threading.Thread(target=consumer,args=[1,])
# c2 = threading.Thread(target=consumer,args=[2,])
# c3 = threading.Thread(target=consumer,args=[3,])
# p = threading.Thread(target=producer,args=["XiaoYu",])
# p2 = threading.Thread(target=producer,args=["LiuYao",])
# c1.start()
# c2.start()
# c3.start()
# p.start()
# p2.start()
