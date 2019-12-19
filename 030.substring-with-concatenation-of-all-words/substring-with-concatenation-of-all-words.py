from collections import deque


class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if len(words) > len(s):
      return []
    d = {}
    t = {}
    ans = []
    deq = deque([])
    wl = len(words[0])#一个单词的长度
    fullscore = 0
    for word in words:
      d[word] = d.get(word, 0) + 1 #word数量加1
      fullscore += 1 #所有词语数量加1

    for i in range(0, len(s)):#遍历每一种候选位置
      head = start = i
      t.clear()
      score = 0

      while start + wl <= len(s) and s[start:start + wl] in d:#当下一个词成立且在words中
        cword = s[start:start + wl]
        t[cword] = t.get(cword, 0) + 1 #匹配到的word的总的匹配次数
        if t[cword] <= d[cword]:#判断cword在这个子字符串中出现的次数是不是一样
          score += 1
        else:#如果字符串中的某个单词量超过了words中出现的数量，则跳出停止这一次的搜索，判断是否符合条件
          break
        start += wl

      if score == fullscore:# 比较score，判断是否一样，如果一样【也就是每个词都找到对应的词】则加入到结果中
        ans.append(head)

    return ans
