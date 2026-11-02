class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # 先將陣列排序
        ans = []
        n = len(nums)

        for i in range(n - 2):
            # 1. 外層第一個數 (i) 的去重：若與前一個數相同，代表該數開頭的所有組合已經找過
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                current_sum = nums[l] + nums[r]

                if current_sum == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # 2. 內層左指標 (l) 去重：跳過重複的元素
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # 3. 內層右指標 (r) 去重：跳過重複的元素
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif current_sum < target:
                    l += 1
                else:
                    r -= 1

        return ans