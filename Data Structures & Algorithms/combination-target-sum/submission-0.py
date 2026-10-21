class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        result = []

        cur = []

        def bt_dfs(index, total):
            if total == target:
                result.append(cur.copy())
                return
            
            if index >= len(nums) or total > target:
                return

            cur.append(nums[index])
            bt_dfs(index, total+nums[index])
            cur.pop()
            bt_dfs(index + 1, total)

        bt_dfs(0,0)

        return result