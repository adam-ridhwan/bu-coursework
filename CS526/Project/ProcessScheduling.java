import java.io.File;
import java.io.PrintWriter;
import java.util.PriorityQueue;
import java.util.Scanner;

public class ProcessScheduling {
    /**
     * ProcessScheduling takes in 4 input parameters of processes
     *
     * parameters: id, priority, duration, arrival time
     * 
     * output: output will be printed on to a separate text file in order of the smallest priority first.
     */
    PriorityQueue<Process> processes;
    PrintWriter writer;

    public ProcessScheduling() throws Exception {
        processes = new PriorityQueue<>();

        // sets output file
        writer = new PrintWriter("process_scheduling_output.txt");

        // read input file
        readFile();
    }

    public static void main(String[] args) throws Exception {

        int currentTime = 0; // current time (incremented after each process)

        int maxWaitTime1 = 10; // first max default variable
        int maxWaitTime2 = 30; // second max default  variable

        // creates new ProcessScheduling
        ProcessScheduling Q = new ProcessScheduling();

        Q.writeFile("\nMaximum wait time 1 = " + maxWaitTime1); // prints 10
        Q.writeFile("Maximum wait time 2 = " + maxWaitTime2); // prints 30

        int n = Q.processes.size(); // total processes

        double totalWaitTime = 0.0; // total wait time

        do {
            // sets first process as null
            assert Q.processes.peek() != null;

            // sets the process with minimum priority
            int minimumPriority = Q.processes.peek().priority;

            // sets the first process to be executed
            Process processToBeExecuted = Q.processes.peek();


            for (Process p : Q.processes) {
                /* finds the process that is lower or equal to current time
                   and with lower priority. sets variable p to processToBeExecuted.
                */
                if (p.arrivalTime <= currentTime) {
                    if (p.priority < minimumPriority) {
                        minimumPriority = p.priority;
                        processToBeExecuted = p;
                    }
                }
            }

            // determines whether a process has completed
            boolean processCompleted = false;

            assert processToBeExecuted != null;
            if (processToBeExecuted.arrivalTime <= currentTime) {
                // checks if the processToBeExecuted has arrived at the current time

                // sets the total wait time for current process
                totalWaitTime += processToBeExecuted.waitingTime;

                // message is initialized to string variable
                String message = "\nProcess removed from queue is: id = " +
                        processToBeExecuted.id + ", at time " + currentTime +
                        ", wait time = " + processToBeExecuted.waitingTime +
                        " Total wait time = " + totalWaitTime +
                        "\nProcess id = " + processToBeExecuted.id +
                        "\n\tPriority = " + processToBeExecuted.priority +
                        "\n\tArrival = " + processToBeExecuted.arrivalTime +
                        "\n\tDuration = " + processToBeExecuted.duration +
                        "\nProcess " + processToBeExecuted.id + " finished at time " +
                        (processToBeExecuted.duration + currentTime +
                                "\n\nUpdate priority:");

                // message is printed on to output text file
                Q.writeFile(message);

                // removes the current process from priority queue
                Q.processes.remove(processToBeExecuted);

                // sets the flag to true when process is completed
                processCompleted = true;

                // increments currentTime variable
                currentTime += processToBeExecuted.duration;

            } else currentTime++;

            if (processCompleted) {
                // if the process is completed, the remaining processes are adjusted

                for (Process p : Q.processes) {
                    // iterates though process queue
                    if (p.arrivalTime <= currentTime) {
                        p.waitingTime = currentTime - p.arrivalTime;
                    }

                    if (p.waitingTime > maxWaitTime2) {
                        /* if process has been waiting for 30, then priority decremented either by 2 or 1
                         */
                        Q.writeFile("PID = " + p.id +
                                ", wait time = " + p.waitingTime +
                                ", current priority = " + p.priority);

                        if (p.priority > 2) {
                            p.priority = p.priority - 2;

                            Q.writeFile("PID = " + p.id +
                                    ", new priority = " + p.priority);

                        } else if (p.priority > 1) {
                            p.priority = p.priority - 1;

                            Q.writeFile("PID = " + p.id +
                                    ", new priority = " + p.priority);
                        }

                    } else if (p.waitingTime > maxWaitTime1) {
                        /* if process has been waiting for 10, then priority decremented either by 1
                         */

                        Q.writeFile("PID = " + p.id +
                                ", wait time = " + p.waitingTime +
                                ", current priority = " + p.priority);

                        if (p.priority > 1) {
                            p.priority = p.priority - 1;

                            Q.writeFile("PID = " + p.id + ", new priority = " + p.priority);
                        }
                    }
                }
            }
        }
        // when all processes are completed, program stops
        while (Q.processes.size() != 0);

        // prints total wait time and average wait time
        Q.writeFile("\nTotal Wait currentTime " + totalWaitTime);
        Q.writeFile("Average Wait currentTime " + totalWaitTime / n);

        // closes the writer
        Q.writer.close();
    }

    // read from input file
    public void readFile() {
        try {Scanner s = new Scanner(new File("process_scheduling_input.txt"));

            while (s.hasNextLine()) {
                // loops through input file
                String[] line = s.nextLine().split(" ");

                // store numbers into list
                int[] lineContents = new int[line.length];

                // iterates through values
                for (int i = 0; i < line.length; i++) lineContents[i] = Integer.parseInt(line[i]);

                writeFile("Id = " + lineContents[0] + ", " +
                        "priority = " + lineContents[1] + ", " +
                        "duration = " + lineContents[2] + ", " +
                        "arrival time= " + lineContents[3]);

                // add new process to priority queue
                processes.add(new Process(
                        lineContents[0], // id
                        lineContents[1], // priority
                        lineContents[2], // duration
                        lineContents[3]) // arrival time
                );
            }
        } catch (Exception ignored) {

        }
    }

    // write to output file
    public void writeFile(String line) {
        writer.append(line).append("\n");
    }
}