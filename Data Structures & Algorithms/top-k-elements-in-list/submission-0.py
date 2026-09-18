class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, count in frequency.items():
            buckets[count].append(number)
        
        result = []

        for count in range(len(nums), 0, -1):
            for number in buckets[count]:
                result.append(number)

                if len(result) == k:
                    return result