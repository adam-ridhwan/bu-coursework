import time 

# StopWatch defined as class with constructor and data fields for startTime, endTime and elapsedTime
class StopWatch:
    def __init__(self, startTime = 0):
        self.__startTime = startTime

    # methods defined for start, stop 
    def start(self):
        self.__startTime = time.time()

    def stop(self):
        return self.getElapsedTime()
    
    # methods getElapsedTime returns the elapsed time
    def getElapsedTime(self):
        elapsedTime = ((time.time() - self.__startTime) * 1000)
        return elapsedTime

# function main() prints result
def main():
    time = StopWatch()
    time.start()
    sum = 0 
    for i in range(1, 1000001):
        sum += i
    time.stop
    print("\nThe sum of numbers from 1 to 1,000,000 is", sum)
    print("The execution time is", time.getElapsedTime(), "milliseconds")
    
main()