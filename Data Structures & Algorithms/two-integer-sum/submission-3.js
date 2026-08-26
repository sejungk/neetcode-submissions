class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let seen = {};
        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (diff in seen) return [seen[diff], i];
            seen[nums[i]] = i;
        }
    }
}
