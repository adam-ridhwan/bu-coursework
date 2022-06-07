import java.util.Random;

public class MultiThreadGenome extends Thread {
    static final String[] multiThreadArray = new String[100];
    static char[] characterArray = new char[]{'A', 'T', 'G', 'C'};
    static Random random = new Random();
    static int size = 0;

    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            StringBuilder randomGenomeSequence = new StringBuilder();
            for (int j = 0; j < 10; j++) {
                int index = random.nextInt(4);
                randomGenomeSequence.append(characterArray[index]);
            }
            String sequence = String.valueOf(randomGenomeSequence);
            multiThreadArray[size++] = sequence;
        }
    }
}
