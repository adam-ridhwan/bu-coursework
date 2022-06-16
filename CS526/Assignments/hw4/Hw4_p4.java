import java.util.Arrays;

public class Hw4_p4 {

    // recursive method
    public static void recursiveFixedSumPairs(int[] a, int i, int j, int k) {
        if (i >= a.length - 1) {
            return;
        }
        if (j >= a.length) {
            recursiveFixedSumPairs(a, i + 1, i + 2, k);
            return;
        }
        // check to see if position i adds position j equals to k
        if (a[i] + a[j] == k) {
            System.out.println("a[" + i + "] = " + a[i] + ", a[" + j + "]=" + a[j]);
        }
        // calls recursive function
        recursiveFixedSumPairs(a, i, j + 1, k);
    }

    // method initializes the input parameters for recursive function
    public static void findFixedSumPairs(int[] a, int k) {
        int i = 0;
        int j = 1;
        recursiveFixedSumPairs(a, i, j, k);
    }

    public static void main(String[] args) {
        int[] a = {1, 5, 8, 11, 14, 15, 20, 23, 25, 28, 30, 34};
        int k = 35;
        System.out.println("k=" + k);
        System.out.println("Given array is:" + Arrays.toString(a));
        findFixedSumPairs(a, k);
    }

}
