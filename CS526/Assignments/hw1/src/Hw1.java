public class Hw1 {

    // receives two integer arrays
    // returns true if they are identical and false otherwise
    public static boolean compare(int[] a, int[] b) {
        // returns false if a and b has the same character length
        if (a.length != b.length) {
            return false;
        }
        else {
            // for-loop checks if each character in a is same as b
            for(int i=0; i<a.length; i++) {
                if(a[i] != b[i]) {
                    return false;
                }
            }
            return true;
        }
    }

    // receives two strings s1 and s2
    // assume length of s1 <= length of s2
    // returns true if s1 is a suffix of s2 and false otherwise
    public static boolean isSuffix(String s1, String s2) {
        // string1 and string2 defined as variables that stores the length of string
        int string1 = s1.length();
        int string2 = s2.length();

        // returns false if length of string1 is more than string2
        if (string1 > string2) {
            return false;
        }
        else {
            // for loop checks to see if each character in string1 is equal to character in string2
            for(int i=0; i<string1; i++) {
                if (s1.charAt(string1 - i - 1) != s2.charAt(string2 - i - 1)) {
                    return false;
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {

        int[] a = {1, 2, 3, 4, 5};
        int[] b = {1, 2, 3, 4, 5};
        int[] c = {1, 2, 3, 40, 5};

        System.out.println("Array a and array b are identical: " + compare(a,b));
        System.out.println("Array a and array c are identical: " + compare(a,c));

        System.out.println();

        String s1 = "def";
        String s2 = "abcdef";
        String s3 = "abcef";

        if (isSuffix(s1,s2)) {
            System.out.println(s1 + " is a suffix of " + s2);
        }
        else {
            System.out.println(s1 + " is not a suffix of " + s2);
        }

        if (isSuffix(s1,s3)) {
            System.out.println(s1 + " is a suffix of " + s3);
        }
        else {
            System.out.println(s1 + " is not a suffix of " + s3);
        }

    }

}