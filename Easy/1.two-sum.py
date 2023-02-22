#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
#題目就是要找出給定數列中兩個元素的和等於目標值的索引位置
class Solution: #定義一個名為Solution的class型別
    #self表示class屬於solution,用nums表示要輸入的數列 target為目標值，->代表會傳回一個數列
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} #創建一個空dict來存儲遍歷過的元素和它們的索引位置
        # 用enumerate枚舉 -> 索引值 元素
        for i, j in enumerate(nums):
            r = target - j  #計算目標值-當前元素剩下的值
            # 判斷剩下的值有沒有在d中，有的話就return這個元素的索引位置和當前元素的索引位置
            if r in d: return [d[r], i]
            d[j] = i    #當前元素加入字典,索引值為i
# @lc code=end

