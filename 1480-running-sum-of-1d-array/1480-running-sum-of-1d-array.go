func runningSum(nums []int) []int {
    var sum []int
    sum = append(sum, nums[0])
    for i := 1; i<len(nums); i++ {
        s := sum[i-1] + nums[i]
        sum = append(sum, s)
    }
    return sum
}