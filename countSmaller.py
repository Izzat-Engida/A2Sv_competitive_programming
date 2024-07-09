class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        answer = [0] * n
        index = list(range(n))

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)
            merge(start, mid, end)

        def merge(start, mid, end):
            left_part = index[start:mid]
            right_part = index[mid:end]
            l, r = 0, 0
            temp = []
            count = 0

            while l < len(left_part) and r < len(right_part):
                if nums[left_part[l]] <= nums[right_part[r]]:
                    answer[left_part[l]] += count
                    temp.append(left_part[l])
                    l += 1
                else:
                    count += 1
                    temp.append(right_part[r])
                    r += 1

            while l < len(left_part):
                answer[left_part[l]] += count
                temp.append(left_part[l])
                l += 1

            while r < len(right_part):
                temp.append(right_part[r])
                r += 1

            for i in range(len(temp)):
                index[start + i] = temp[i]

        merge_sort(0, n)
        return answer

