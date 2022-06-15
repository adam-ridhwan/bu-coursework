import java.util.Arrays;

public class Hw4_p3 {

    // Rearrange strings that have less than or equal to x to the left and the rest to the right.
    public static void recursiveRearrange (String[] a, int x, int left, int right) {

        // condition to check if left pointer crosses the right pointer.
        if (left > right)
            return;

        // checks to see if the string length of left index is <= x, if true = moves on to the next index
        if (a[left].length() <= x) {
            recursiveRearrange(a, x, left + 1, right);
        } else {
            // checks to see if the string length at the right index <= x, if true: string is swapped from the left
            // to the right index
            if (a[right].length() <= x) {
                String temp = a[left];
                a[left] = a[right];
                a[right] = temp;
                recursiveRearrange(a, x, left + 1, right - 1);
            } else {
                recursiveRearrange(a,x,left,right-1);
            }
        }
    }

        public static void rearrange (String[]a,int x){
            // implement this method
            // consider writing a separate method with additional parameters
            int left = 0, right = a.length-1;
            recursiveRearrange(a,x,left,right);
        }

        public static void main (String[]args){

            String[] stringArray = {"data", "structures", "and", "algorithms", "in", "java"};

            System.out.println();
            int x = 4;
            System.out.println("Array before change: " + Arrays.toString(stringArray));
            rearrange(stringArray, x);
            System.out.println("Array before change: " + Arrays.toString(stringArray));

        }
    }
