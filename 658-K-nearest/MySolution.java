/*My solution -- AC'ed but took 30+ minutes to code.*/

public class Solution {
    public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
        // Binary search to find x; and then populate the solution
        int start = 0, end = arr.size(), mid;

        while (end - start > 1) {
            mid = (start + end) / 2;
            if (arr.get(mid) < x) {
                start = mid;
            } else if (arr.get(mid) > x){
                end = mid;
            } else {
                break;
            }
        }
        mid = (start + end) / 2;
        // Now mid is the index of the element closest to x in the array
        //System.out.println("mid=" + mid);

        List<Integer> res = new ArrayList<Integer>();
        int left = mid - 1, right = mid + 1, added = 0;

        res.add(arr.get(mid));
        added++;

        while (added < k) {

            if (left == -1) {
                for (int i = 0; added < k; i++) {
                    res.add(arr.get(right));
                    right++;
                    added++;
                }
                Collections.sort(res);
                return res;
            }
            if (right == arr.size()) {
                for (int i = 0; added < k; i++) {
                    //System.out.println("left=" + left + ", right=" + right + "; added=" + added + "; k=" + k);
                    res.add(arr.get(left));
                    left--;
                    added++;
                }
                Collections.sort(res);
                return res;
            }
            //System.out.println("left=" + left + ", right=" + right + "; added=" + added + "; k=" + k);
            if (Math.abs(x - arr.get(left)) <= Math.abs(arr.get(right) - x)) {
                res.add(arr.get(left));
                left--;
                added++;
            } else {
                res.add(arr.get(right));
                right++;
                added++;
            }
        }

        //System.out.println("res before sotring is " + Arrays.asList(res));
        Collections.sort(res);
        return res;

    }
}
