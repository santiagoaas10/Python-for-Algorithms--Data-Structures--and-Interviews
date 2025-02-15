def maxSubArray(nums):
    current_sum = nums[0]  # Suma máxima terminando en el índice actual
    max_sum = nums[0]  # Suma máxima encontrada

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        
        max_sum = max(max_sum, current_sum)

    return max_sum


maxSubArray([1,2,-1,3,4,10,10,-10,-1])