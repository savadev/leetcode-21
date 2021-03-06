// 3Sum Closest

// Problem 16
// Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

// Example:
// Given array nums = [-1, 2, 1, -4], and target = 1.
// The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
  let closestSum = nums[0] + nums[1] + nums[2],
    smallestDiff = Math.abs(target - closestSum);

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        let setSum = nums[i] + nums[j] + nums[k];
        if (setSum == target) {
          return setSum;
        }

        let diff = Math.abs(target - setSum);
        if (diff < smallestDiff) {
          closestSum = setSum;
          smallestDiff = diff;
        }
      }
    }
  }

  return closestSum;
};

module.exports = threeSumClosest;
