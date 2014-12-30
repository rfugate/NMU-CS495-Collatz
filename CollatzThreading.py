import time
import threading

class Collatz(threading.Thread):
    def __init__(self,n):
        self.n = n
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 1:
            raise StopIteration
        else:
            if self.n % 2 == 0:
                self.n //= 2
                return self.n
            else:
                self.n = 3 * self.n + 1
                return self.n


d = {}                                              #Empty Dictionary
lock = threading.Lock()                             

def main():
    startTime = time.time()
    thread1 = threading.Thread(target = buildCollatz, args = (1,500000))            #thread1 will compute 1 - 500,000
    thread2 = threading.Thread(target = buildCollatz, args = (500000,1000000))      #thread2 will compute 500,000 - 1,000,000
    thread1.start()                                                                 #This cuases the thread to run
    thread2.start()
    thread1.join()                                                                  #This waits until the thread has completed
    thread2.join()
    endTime = time.time()

    maxValue = max(d, key = d.get)                                                  #Finds the maximum value in dictionary
    longestValues = [s for s in d if d[s] == d[maxValue]]                           #Finds all Keys in dictionary with maxValue
    
    #print(d)
    print("Total time taken: ", endTime - startTime)
    print("Longest Sequence(s): ", longestValues, " = ", d[maxValue])
    
def buildCollatz(self, end):
    for x in range(self, end):
        count = 0
        for y in Collatz(x):
            count += 1
            if y == 1:                              #If y == 1 then no previous matches were found - Add total count to dictionary
                lock.acquire()
                d[x] = count
                lock.release()
            if y in d:                              #If y == previous y in dictionary then add that count to your current count value
                lock.acquire()
                d[x] = count + d[y]
                lock.release()
                break;

main()



