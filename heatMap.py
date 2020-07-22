#Samuel Parmer
#sap18bq


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():
    temp = int(input("Enter starting temp "))
    current = np.zeros(shape=(temp +2, temp +2))

    #current[1:temp+1,1] = temp  #ask for explanation on numpy indexing/slicing. Why 1:temp+1?
    current[0:temp+3,0] = temp
    previous = current.copy()

    counter = 0

    jRange = 1
    #plot each point individually with 2 for loops using .plot
    #break up the temps into 4 ranges and assign colors based on the range


    color = None

    while(counter <= 3000 and counter != temp): #limit iterations at 3000 or when counter = temp

        # for j in range(1,temp-1):
        #     for i in range(2,temp-1):

        for i in range(1,temp+1):
            previous = np.array(current)
            for j in range(1,temp+1):

                current[i, j] = (previous[i - 1, j] + previous[i + 1, j] + previous[i, j - 1] + previous[i, j + 1])/4
                #calculate matrix

            if np.array_equal(current,previous):
                break   #convergence, end loop

                 # continue loop, copy current frame to previous frame
                #convergence
        counter = counter + 1
        jRange = jRange+1
        print(counter)


    print(current)
    #Plot all points, choose color per point
    for p in range(0,temp+1):
        for q in range(0, temp+1):
            if (current[p, q] < temp / 8):
                color = 'darkblue'

            elif (current[p, q] < temp / 7):
                color = 'blue'

            elif (current[p, q] < temp / 6):
                color = 'aqua'

            elif (current[p, q] < temp / 5):
                color = 'lawngreen'

            elif (current[p, q] < temp / 4):
                color = 'yellow'

            elif (current[p, q] < temp / 3):
                color = 'orange'

            elif (current[p, q] < temp / 2):
                color = 'red'

            else:
                color = 'darkred'

            plt.plot(q, p, 'or', markersize=3, c=color)


    plt.xlim([-1, temp+1])       #set x, y axis bounds
    plt.ylim([-1, temp+1])
    plt.show()

#make grid with (temp+2)*temp




if __name__ == "__main__":
        main()