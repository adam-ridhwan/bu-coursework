import java.util.Arrays;

public class Hw4 {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        SingleThreadGenome.run();
        long endTime = System.nanoTime();
        long totalTime = endTime - startTime;

        System.out.println(ThreadColor.ANSI_RESET + Arrays.toString(SingleThreadGenome.singleThreadArray) + "\n");
        System.out.println("\n" + ThreadColor.ANSI_RED + "Running time of single thread = " + String.format("%,d",
                totalTime) + " nanoseconds\n\n");

        long multiStartTime = System.nanoTime();
        for (int i = 0; i < 5; i++) {

            if (i > 0) System.out.println(ThreadColor.ANSI_BLUE + "Thread = " + i);

            Thread multiThread = new MultiThreadGenome();
            multiThread.start();

            if (i > 0) {
                System.out.println(ThreadColor.ANSI_RESET + Arrays.toString(MultiThreadGenome.multiThreadArray) + "\n");
            }
        }

        long multiEndTime = System.nanoTime();
        long multiTotalTime = multiEndTime - multiStartTime;

        System.out.println(ThreadColor.ANSI_BLUE + "Final Thread: -");
        System.out.println(ThreadColor.ANSI_RESET + Arrays.toString(MultiThreadGenome.multiThreadArray));
        System.out.println("\n" + ThreadColor.ANSI_BLUE + "Running time of multi thread = " + String.format("%,d",
                multiTotalTime) + " " + "nanoseconds");
    }
}
