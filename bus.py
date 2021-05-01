# Using dynamic programming

def getTotalPassengers(stops):
    if stops == 1:
        return 1
     
    totalPassengers = 0
    totalPassengers += getTotalPassengers(stops - 1)

    totalPassengers += totalPassengers + 1

    return totalPassengers



T = int(input())

for i in range(T):
    stops = int(input())
    print(getTotalPassengers(stops))
