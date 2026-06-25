int countMajoritySubarrays(int* nums, int numsSize, int target) {
    int total_subarrays = 0;
    for (int i = 0; i < numsSize; i++) {
        int balance = 0;
        for (int j = i; j < numsSize; j++) {
            if (nums[j] == target) {
                balance += 1;
            } else {
                balance -= 1;
            }
            if (balance > 0) {
                total_subarrays++;
            }
        }
    }
    return total_subarrays;
}