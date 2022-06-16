public class Hw7_p4 {

    public static void chainingMethod(SinglyLinkedList[] T, int[] a) {
        // implement this method
        System.out.println();

        for (int i : a) {
            boolean exists = false;
            int hash = i % T.length;
            SinglyLinkedList.Node temp = T[hash].getHead();

            while (temp != null) {
                if (temp.getElement() == i) {
                    exists = true;
                    System.out.println("Element " + i + " already exists");
                    break;
                }
                temp = temp.getNext();
            }

            if (exists) {
                continue;
            }
            T[hash].addLast(i);
        }
    }


    public static void main(String[] args) {
        // complete the main method

        int N = 5; // hash table size

        // create and initialize an array of SinglyLinkedList
        SinglyLinkedList[] T = new SinglyLinkedList[N];
        for (int i = 0; i < T.length; i++) {
            T[i] = new SinglyLinkedList();
        }

        // array of integer keys
        int[] a = {3, 5, 10, 3, 18, 54, 26, 3, 75, 9, 11, 5, 29, 34};

        // insert keys
        chainingMethod(T, a);

        // print hash table content
        System.out.println();
        System.out.println("Hash table content:");
        System.out.println();

        for (int i = 0; i < T.length; i++) {
            String output = "Hash table slot " + i + ": " + T[i];
            System.out.println(output.replaceAll("[(),]",""));
        }
    }
}