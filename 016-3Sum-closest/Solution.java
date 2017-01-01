public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // Alg 1: Brute force + dynamically store : O(n^3) time, O(n^3) space
        // Alg 2: For each of the first number, htable {sum -> combs} and keep the closest to target. O(n^3) time + O(n^2) space if only the values htable;
        /*
        // Alg 3: For each of the first number, for each of second number, search in hash table from 0 to curr minimum sum. O(n^3) time + O(n) space. Assume nums has no duplicated values.
        if (nums.length < 3) {
            System.out.println("Illegal input!");
            return 0;
        }
        Arrays.sort(nums);
        HashMap<Integer, Integer> v2p = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            v2p.put(nums[i], i);
        }
        int first, second, third;
        int minsum = nums[0] + nums[1] + nums[2];
        int minabsdiff = Math.abs(minsum - target);
        for (first = 0; first < nums.length - 2; first++) {
            for (second = first+1; second < nums.length - 1; second++) {

                for (int k = target - minabsdiff; k < target + minabsdiff; k++) {
                    if (k == nums[first] || k == nums[second])
                        continue;
                    if (v2p.containsKey(k)) {
                        int cursum = nums[first] + nums[second] + k;
                        int curabsdiff = Math.abs(cursum - target);
                        if (curabsdiff < minabsdiff) {
                            minsum = cursum;
                            minabsdiff = curabsdiff;
                        }
                    }
                }

            }
        }
        return minsum;
        */
        /*
        // Alg 4: First sort the array. O(n^2 log(n)) time using binary search for the third element. Update the minabsdiff and minsum. Accepted but quite slow.
        Arrays.sort(nums);
        int first, second, third;
        int minsum = nums[0] + nums[1] + nums[2];
        int minabsdiff = Math.abs(minsum - target);
        for (first = 0; first < nums.length - 2; first++) {
            for (second = first+1; second < nums.length-1; second++) {
                int start = second + 1;
                int end = nums.length-1;
                while (end - start > 1) {
                    int mid = start + (end - start) / 2;
                    if (nums[first] + nums[second] + nums[mid] == target) {
                        return target;
                    } else if (nums[first] + nums[second] + nums[mid] < target) {
                        start = mid;
                    } else {
                        end = mid;
                    }
                }
                int s1 = nums[first] + nums[second] + nums[start];
                int d1 = Math.abs(s1 - target);
                int s2 = nums[first] + nums[second] + nums[end];
                int d2 = Math.abs(s2 - target);
                int curmindiff = d1, curminsum = s1;
                if (d2 < d1) {
                    curmindiff = d2; curminsum = s2;
                }
                if (curmindiff < minabsdiff) {
                    minabsdiff = curmindiff; minsum = curminsum;
                }
            }
        }
        return minsum;
        */
        // Alg 5: Canonical 2-pointer pass with O(n^2) time and O(1) space. Remember: on a sorted array, binary search uses O(log n) time to locate one variable; but 2-pointer pass uses O(n) time to locate two variables.
        Arrays.sort(nums);
        int i, j, k;
        int minsum = nums[0] + nums[1] + nums[2];
        int minabsdiff = Math.abs(minsum - target);
        for (i = 0; i < nums.length-2; i++) {
            j = i+1;
            k = nums.length-1;
            int dir = 1;

            while (j < k) {
                int currsum = nums[i] + nums[j] + nums[k];
                int currdiff = Math.abs(currsum - target);
                if (currdiff < minabsdiff) {
                    minabsdiff = currdiff;
                    minsum = currsum;
                }
                if (currsum == target) {
                    return target;
                } else if (currsum < target) {
                    j++;
                    dir = 1;
                } else {
                    k--;
                    dir = -1;
                }

            }

        }
        return minsum;
    }
}
