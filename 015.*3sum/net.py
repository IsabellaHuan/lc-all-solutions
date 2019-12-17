#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 下午5:38
# file : net
"""
NOTICE:
三元素和为零
嵌套遍历套路：确定最小（大的），然后内层循环只要遍历一侧就可以
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        first=[]
        i=0
        while(i<len(nums)-2): # 遍历组合中最小的数
            if(nums[i]!=nums[i-1] or i==0):
                target=0-nums[i] # 剩下两个元素的和
                left=i+1
                right=len(nums)-1 # 为什么不可能是小于自己的数和大于自己的数加和为自己的负数[最外层是三数中最小数循环，所以内层只要看大于外层元素的组合就可以]
                while(left!=right):
                    if(nums[left]+nums[right]==target):
                        first.append([nums[i],nums[left],nums[right]]) # 找到一个目标组合
                        while(left<right):
                            left+=1
                            if(nums[left]!=nums[left-1]): # 判断是否有重复的数字，如果有重复数字，则继续头指针后移
                                break
                        while(right>left):
                            right-=1
                            if(nums[right]!=nums[right+1]):# 判断是否有重复的数字，如果有重复数字，则继续尾指针后移
                                break
                    elif(nums[left]+nums[right]>target):#判断与target的距离，决定如何移动：大了则移动尾指针，小了移动头指针
                        right-=1
                    elif(nums[left]+nums[right]<target):
                        left+=1
            i+=1
        return first