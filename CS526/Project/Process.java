class Process implements Comparable<Process> {
    int id, priority, duration, arrivalTime, waitingTime;

    // variables are initialized as integers from input file
    public Process(int i, int p, int d, int at) {
        id = i;
        priority = p;
        duration = d;
        arrivalTime = at;
        waitingTime = 0;
    }

    @Override
    public int compareTo(Process p) {
        if (this.priority < p.priority &&
                this.arrivalTime < p.arrivalTime)
            return 1;
        else if (this.priority > p.priority &&
                this.arrivalTime > p.arrivalTime)
            return -1;
        else if (this.priority < p.priority &&
                this.arrivalTime > p.arrivalTime)
            return -1;
        else if (this.priority > p.priority &&
                this.arrivalTime < p.arrivalTime)
            return 1;
        else return 0;
    }
}