class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        result = []

        current = []

        def bt_dfs(index, total):
            if target == total:
                result.append(current.copy())
                return
            
            if index >= len(nums) or total > target:
                return

            current.append(nums[index])
            bt_dfs(index, total + nums[index])

            current.pop()
            bt_dfs(index + 1, total)

        bt_dfs(0,0)
        return result