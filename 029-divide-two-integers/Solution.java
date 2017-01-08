// Divide two integers without using multiplication, division, or mod.
// When overflow occurs, output either Integer.MAX_VALUE or Integer.MIN_VALUE
public class Solution {
    public int divide(int dividend, int divisor) {
        long res = 0;
        long a = dividend, b = divisor;

        if (a == Integer.MIN_VALUE && (b == 1 || b == -1))
            return b==-1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;

        int sign = 1;
        if (a < 0 && b < 0) {
            a = -a;
            b = -b;
            sign = 1;
        } else if (a < 0) {
            a = -a;
            sign = -1;
        } else if (b < 0) {
            b = -b;
            sign = -1;
        }


        if (b == 0) return Integer.MAX_VALUE;
        //System.out.println("a=" + a + ",b=" + b + ",sign=" + sign);

        long sum = b;
        int pow = 1;
        long resp = 1;
        while (b <= a) {
            sum = b;
            resp = 1;
            while (sum + sum <= a) {
                sum += sum;
                pow += pow;
                resp += resp;
                //System.out.print(sum + " ");
            }

            a -= sum;
            res += resp;
            //System.out.println("");
            //System.out.println("a=" + a);
        }

        //System.out.println("res=" + res);
        return sign==1 ? (int)res : (int)(-res);
    }
}
