#coding=utf-8
# author : huanshuwen
# time : 下午11:27
# file : mine
"""
NOTICE:
1001，2002，2112
# 几位数只知道的
# 按照回文的定义进行逐项判断
# int32：-2147483648~2147483647
"""
def check_palindrome(num):
    length=10
    result=True
    while num/pow(10, length)==0:
        length -=1
    length=length+1 #长度和数量级的区别
    while num>0:
        max_i = num/pow(10,length-1)
        min_i = num%10
        print(num,length,max_i,min_i)
        if max_i==min_i:
            num = (num/10)%pow(10,length-2)#注意新数的生成
            length = length - 2
        else:
            result=False
            break
    return result
if __name__=='__main__':
    num=4554
    print(check_palindrome(num))


