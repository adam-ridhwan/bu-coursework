import java.util.Arrays;
import java.util.Random;

public class Hw4 {
    public static void main(String[] args) throws InterruptedException {
        /* implementation of single thread */
        long startTime = System.nanoTime(); // starts the timer
        SingleThreadGenome.run(); // calls the single thread class run()
        long endTime = System.nanoTime(); // stops the timer
        long totalTime = endTime - startTime; // gets the total time

        // prints result of single thread
        System.out.println(ThreadColor.ANSI_RED + "Array results for no thread: -");
        System.out.println(ThreadColor.ANSI_RESET + Arrays.toString(SingleThreadGenome.singleThreadArray));
        System.out.println(ThreadColor.ANSI_RED + "Running time of single thread = " +
                            String.format("%,d", totalTime) + " nanoseconds\n");


        /* main implementation of multi thread concurrency */
        long multiStartTime = System.nanoTime(); // starts the timer
        for (int i = 0; i < 5; i++) {
            // loop creates 5 new threads
            Thread multiThread = new MultiThreadGenome(); // initialize thread each loop
            multiThread.start(); // calls the start function for multi thread class
            if (i == 4) {
                multiThread.join(); // joins the last thread to print result
            }
        }
        long multiEndTime = System.nanoTime(); // stops timer
        long multiTotalTime = multiEndTime - multiStartTime; // gets the total time

        // prints result of multi thread
        System.out.println(ThreadColor.ANSI_BLUE + "Array results for multi thread: -");
        System.out.println(ThreadColor.ANSI_RESET + Arrays.toString(MultiThreadGenome.multiThreadArray));
        System.out.println(ThreadColor.ANSI_BLUE + "Running time of multi thread = " +
                           String.format("%,d", multiTotalTime) + " " + "nanoseconds");
    }

    // colors for results on console
    public static class ThreadColor {
        public static final String ANSI_RESET = "\u001B[0m";
        public static final String ANSI_RED = "\u001B[31m";
        public static final String ANSI_BLUE = "\u001B[34m";
    }

    // single thread function class
    public static class SingleThreadGenome {
        static final String[] singleThreadArray = new String[100]; // holds 100 sequence
        static char[] characterArray = new char[]{'A', 'T', 'G', 'C'}; // characters for sequence
        static Random random = new Random(); // random function
        static int size = 0; // index for singleThreadArray

        // single thread function
        public static void run() {
            while (size != 100) {
                // while the size variable is not 0, continue
                StringBuilder randomGenomeSequence = new StringBuilder(); // creates the string sequence
                for (int j = 0; j < 10; j++) {
                    // loop until a 10 character sequence is created
                    int index = random.nextInt(4); // chooses random number from 1-4
                    randomGenomeSequence.append(characterArray[index]); // appends random character to randomGenomeSequence
                }
                String sequence = String.valueOf(randomGenomeSequence); // variable created for the random genome
                singleThreadArray[size++] = sequence; // adds the sequence to the singleThreadArray;
            }
        }
    }

    // multi thread function class
    public static class MultiThreadGenome extends Thread {
        static final String[] multiThreadArray = new String[100]; // holds 100 sequence
        static char[] characterArray = new char[]{'A', 'T', 'G', 'C'}; // characters for sequence
        static Random random = new Random(); // random function
        static int size = 0; // index for multiThreadArray

        // multi thread function
        @Override
        public void run() {
            for (int i = 0; i < 20; i++) {
                // loop 20 times
                StringBuilder randomGenomeSequence = new StringBuilder(); // create the string sequence
                for (int j = 0; j < 10; j++) {
                    // loop until a 10 character sequence is created
                    int index = random.nextInt(4); // chooses random number from 1-4
                    randomGenomeSequence.append(characterArray[index]); // appends random character to randomGenomeSequence
                }
                String sequence = String.valueOf(randomGenomeSequence); // variable created for the random genome
                multiThreadArray[size++] = sequence; // adds the sequence to the multiThreadArray;
            }
        }
    }
}
