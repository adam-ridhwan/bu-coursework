import java.util.Random;

public class SingleThreadGenome {
    static final String[] singleThreadArray = new String[100];
    static char[] characterArray = new char[]{'A', 'T', 'G', 'C'};
    static Random random = new Random();
    static int size = 0;

    public static void run() {
        while (size != 100) {
            StringBuilder randomGenomeSequence = new StringBuilder();
            for (int j = 0; j < 10; j++) {
                int index = random.nextInt(4);
                randomGenomeSequence.append(characterArray[index]);
            }
            String sequence = String.valueOf(randomGenomeSequence);
            singleThreadArray[size++] = sequence;
        }
    }
}

