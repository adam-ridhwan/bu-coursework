# Homework 4

Homework 4 is about concurrency

## Description

***Homework 4 compares the runtime of single vs multithread of creating genome sequence***

--

### 1. Single Thread Function - SingleThreadGenome

The single thread function class creates 100 random genome sequences linearly

```
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
```

####Variables: -

1. **singleThreadArray** is an array with type string to hold 100 randomly generated genome sequence
2. **characterArray** is an array with type char that holds characters:  A, T, G, C
3. **random** is the java randomize function
4. **size** is the index for **singleThreadArray**

####Thread function: -

1. while-loop loops through the function 100 times to fill up the **singleArrayArray**
2. A stringBuilder variable (**randomGenomeSequence**) is created to hold the random generated sequence
3. for-loop loops 10 times until a 10 character sequence is generated.
4. A random number from 1-4 is chosen randomly to choose the index value of **characterArray**
5. The random chosen character is then added to **randomGenomeSequence**)
6. When there is 10 characters in **randomGenomeSequence**, it is then added to **singleThreadArray**

--
### 2. Multi Thread Function - MultiThreadGenome

The multi thread function class creates 20 random genome sequences 5 times concurrently. 

```
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
```
####Variables: -

1. **multiThreadArray** is an array with type string to hold 100 randomly generated genome sequence
2. **characterArray** is an array with type char that holds characters:  A, T, G, C
3. **random** is the java randomize function
4. **size** is the index for **multiThreadArray**

####Thread function: -

1. for-loop loops through the function 20 times to fill up the **multiArrayArray**
2. A stringBuilder variable (**randomGenomeSequence**) is created to hold the random generated sequence
3. for-loop loops 10 times until a 10 character sequence is generated.
4. A random number from 1-4 is chosen randomly to choose the index value of **characterArray**
5. The random chosen character is then added to **randomGenomeSequence**)
6. When there is 10 characters in **randomGenomeSequence**, it is then added to **multiThreadArray**

--


### Main()

### 3a. single thread implementation

```
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
```

1. Start timer is first initialized
2. **SingleThreadGenome.run()** is called to perform the function
3. Timer is ended and total time is calculated
4. Results are printed

Example of result: -

```
Array results for no thread: -
[CGAATCTACT, TCAACCCCCG, ATTTTCAAGA, TCGCTCTACG, TGAGATACAT, GCCCATACAA, CTTAGTACTC, TGGCTTAGAT, AACACCTTGG, AGAGTACAAA, 
ACCAACTATG, TGCTGGAACG, TAGACGAATC, CATATATATG, CTATTCGGAG, ATCCGCCTCA, AACGAAGATG, GACCGGTCGT, CGTGTGGTGT, TCCCTAGGCG,
AACCAGCAGT, CCGTTGCCAG, TGCCGGGTCG, ATTGTGGCCC, ACCCAAGAGG, ACACCCAGCG, ATTACTTATT, TTACAGGGGC, GGCAATCGTG, CCCGCCACGC, 
CTTTAGTTCA, GACAAAGCCA, AACTACACGG, CGCGGGTATC, AGACGGGAGC, GAACAATTCT, CTGTGGTTCC, AGACGTTTCC, ATAATTTTTG, TCAAAACTCT, 
TCGCCCGTTG, AGAGTGTGAT, TCATGAGGGG, CAGTCGGTTA, GTTTTCCCCA, ACAAATCGCA, TCCTGCACTC, ACGCGACGTA, CATTAACACA, GCCGACGTGG, 
CTTGCTCTCA, CGTCATACAC, ACTAGCGCCC, CCGGACGGTG, CTCTGTGGCA, CTTCGCCAAT, GGCCCCAGTT, GGACCAAGAG, GTGGCTAGGT, GAGTGTAGAT, 
GACTGAGTAT, GAAGCCGCTG, GGCGGCGATA, ATATTGCTGA, AGTCCCTCTC, CAGCGGACTT, GTGCATATGG, AGACCTCAGC, CGCACCTGCC, GGTGCCATTA, 
ACCAGGACGA, GACTATATGA, TACCCGTCGC, TGGCGATTAT, CTATATTTTT, TAAAGGTCGG, TGTCAGCTCT, CCGGGCCAAT, TGGCCAAAGT, GAGTCGTTCA, 
TCATAATTGA, GACAACTGAA, CTGACACGTA, ATAAAATTGG, TTAGGAGGAA, TAGTCGTACA, TAGAGAGTAG, CGAACTAGAC, AATCAAATAC, TAGTTACACT, 
CAGAGGGCCG, ACGGCCCCGG, AAATATTGTG, CGATTGCAGT, GGTGTAGTGT, TCATCCGATA, GCTGAGTCAG, TCGCGACCCC, CTACGCGGCG, AATCGGGCCT]
Running time of single thread = 1,737,921 nanoseconds

```
<br>


### 3b. mutli thread implementation

```
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
```

1. start timer is first initialized
2. for-loop used to create 5 threads
3. thread is created each loop
4. the last thread joins the results to avoid printing any null values from **multiThreadArray**
5. Timer is ended and total time is calculated
6. results are printed

Example of result: -

```
Array results for multi thread: -
[CGATTCACAG, TGAAAATCAA, ACAGGTCATT, CTGCTCACCA, AGCGTCGCGA, TCTTTTGGTT, ATCCGATATG, ACGCATGTCC, GTTGCGAAGA, GATCAGATGT, 
GGCCTTTCAC, TAGTCTCATC, CCATAATATG, TCATCGCAAC, ACGCAGTTAA, GGGCGCCGCT, GTCCTAAGCG, TAGTGTGGGG, ATAGGTAGGA, CCTCTGGAGG, 
GCCGAACTCA, TGTAAGGAAG, ATCTTTACCT, TACCTTGGCT, AGGACTCGTA, GCTCCGAAGA, GGAAAGGCTA, AGGGAAACGG, TCTATATCTT, GATTATGATA, 
GGATATTTAC, ATGTGCAAAA, ACCAGTATAA, TGAAATCTGA, TCGAGCCCTT, GCCTGTGACG, CTACAGCGTT, TGGGTACATA, GCCGTGTAAT, TATACGGCAT, 
AGCGTACGCA, GGCGTGGGCA, CGTAACAAAC, CAGTGCCCTA, AGCTCCTGTA, AGGTGGAATG, ACGGCTAGAA, ATCTCGGATT, CAGCGTGAGA, ACGACTCGAA, 
AATACTCGGG, AACACAGCTC, ATCTGGCTCG, CTTACTCACC, CTCCCGCGTT, TCGCTACCTG, CATTGCCTAT, GCACGGGAGG, CCAGGTACTC, ATGGACACGC, 
GGCTAGTTCT, ACTGTGATTC, GGTCTATGTA, GTATTCCCCT, CACCCTCTGT, AGTCCGTCTC, TTGAATACCT, AGGCCGATGC, CAGCCCGCAG, TTGAGTCAAG, 
TTATTCAAGA, AGGCCCTTAT, GGTGGGGCAA, TTCTGCGTGA, AACTACAGGC, TGTCCGTCAT, GTCACTTGAA, ATTGCGGTCT, ATTGTGGCTG, ATCCGCAGGC, 
CCGTGCTGAC, GGAGATTAGA, GCAGAATTGG, ACCTTCGTGA, CGGATCACAG, ATAACCGACA, AGTTACGTTA, TAGGGGATGA, TGCGTTTCTA, AATAACAACC, 
CTATTATCGG, GATTCTGGTA, CAAGTCTTTT, AGTGCCGGCT, TCCAGTTGCG, ATGAACTCTG, AATGTATTGC, ACGGCGCCGC, TTTGGTGAGG, AATATGGTTG]
Running time of multi thread = 729,780 nanoseconds
```


