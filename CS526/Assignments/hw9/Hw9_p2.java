import java.util.Random;

public class Hw9_p2 {
    static int n = 10;
    static int[] a = new int[n];

    public static void main(String[] args) {
        System.out.println("First Program:-");
        FirstProgram();

        System.out.println("\nSecond Program:-");
        SecondProgram();

    }

    private static void FirstProgram() {
        int insertionSum = 0;
        int quickSum = 0;

        for (int i = 0; i < 10; i++) {

            GenerateNumbers();

            int[] aCopyForInsertion = a.clone();
            int[] aCopyForQuickSort = a.clone();

            long insertStartTime = System.nanoTime();
            InsertionSort(aCopyForInsertion);
            long insertEndTime = System.nanoTime();
            long insertTotalTime = (insertEndTime - insertStartTime) / 1000;
            insertionSum += insertTotalTime;

            long quickStartTime = System.nanoTime();
            QuickSort(aCopyForQuickSort, 0, 10 - 1);
            long quickEndTime = System.nanoTime();
            long quickTotalTime = (quickEndTime - quickStartTime) / 1000;
            quickSum += quickTotalTime;
        }
        System.out.println("Average Insertion Time " + insertionSum / a.length + " microseconds");
        System.out.println("Average Quick Sort Time " + quickSum / a.length + " microseconds");
    }

    private static void SecondProgram() {
        int insertionSum = 0;
        int quickSum = 0;

        int[] n = {15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100};

        for (int i = 0; i < 18; i++) {

            int[] aCopyForInsertion = n.clone();
            int[] aCopyForQuickSort = n.clone();

            long insertStartTime = System.nanoTime();
            InsertionSort(aCopyForInsertion);
            long insertEndTime = System.nanoTime();
            long insertTotalTime = (insertEndTime - insertStartTime) / 1000;
            insertionSum += insertTotalTime;

            long quickStartTime = System.nanoTime();
            QuickSort(aCopyForQuickSort, 0, 10 - 1);
            long quickEndTime = System.nanoTime();
            long quickTotalTime = (quickEndTime - quickStartTime) / 1000;
            quickSum += quickTotalTime;
        }
        System.out.println("Average Insertion Time " + insertionSum / n.length + " microseconds");
        System.out.println("Average Quick Sort Time " + quickSum / n.length + " microseconds");
    }

    private static void Summary() {
        int[] n = {15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100};

        int[] aCopyForInsertion = n.clone();
        int[] aCopyForQuickSort = n.clone();

        System.out.println("Insertion Sort");
        InsertionSort(aCopyForInsertion);

        System.out.println("\nQuick Sort");
        QuickSort(aCopyForQuickSort, 0, n.length - 1);
    }

    private static void GenerateNumbers() {
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            a[i] = rand.nextInt(10_000);
        }
    }

    private static void InsertionSort(int[] array) {

        for (int i = 1; i < array.length; i++) {
//            long start = System.nanoTime();
//            System.out.print(array[i] + " ");
            var current = array[i];
            var j = i - 1;
            while (j >= 0 && array[j] > current) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = current;
//            long end = System.nanoTime();
//            long total = (end - start) / 1000;
//            System.out.println(total);
        }
    }

    public static void QuickSort(int[] array, int start, int end) {

        if (start < end) {


            int partitionIndex = partition(array, start, end);

            QuickSort(array, start, partitionIndex - 1);
            QuickSort(array, partitionIndex + 1, end);

//            long startTime = System.nanoTime();
//            System.out.print(array[partitionIndex] + " ");
//            long endTime = System.nanoTime();
//            long totalTime = (endTime - startTime) / 1000;
//            System.out.println(totalTime);
        }
    }

    private static int partition(int[] array, int start, int end) {
        int pivot = array[end];
        int i = (start - 1);

        for (int j = start; j < end; j++) {
            if (array[j] <= pivot) {
                i++;

                int swapTemp = array[i];
                array[i] = array[j];
                array[j] = swapTemp;
            }
        }

        int swapTemp = array[i + 1];
        array[i + 1] = array[end];
        array[end] = swapTemp;
        return i + 1;
    }

}
