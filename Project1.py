from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
import matplotlib.pyplot as plt

#adding python file path name

#FUNCTIONS
def my_h2_function(x):

    #splitting x and y coordinates apart
    x_cor = x[:,0]
    y_cor = x[:,1]


    #calculate value for coordinate and then append it to list
    output = np.power(x_cor,2)+ np.power(y_cor,2)

    return output

def my_h_function(x):

    #splitting into x and y coordinates
    x_cor = x[:,0]
    y_cor = x[:,1]

    #use numpy operations to calculate h function 
    output = np.power(x_cor, 3) + np.power(y_cor, 2) + 2 * x_cor * y_cor - np.sin(x_cor) + np.cos(2 * np.pi * x_cor * y_cor ) - 1

    return output

def my_g_function(x):

    #splitting into x and y coordinates
    x_cor = x[:,0]
    y_cor = x[:,1]
    
    #use numpy operations to calculate g function 
    output = (1 / (2 * np.pi) ) * np.exp( (-1) * (np.power(x_cor, 2) + np.power(y_cor, 2) ) / 2 )
    
    return output


def plot_scatter(x):

    sp_x = [] #x coordinates for sample space
    sp_y = [] #y coordinates for sample space 
    nonsp_x = []#x coordinates not in sample space
    nonsp_y = []#y coordinates not in sample space

    sp_g = []#g values that are in sample space
    nonsp_g = []#g values not in sample space
    
    h = my_h_function(x)#value to determine whether a coordinate is in sample space or not 
    g = my_g_function(x)#z values for scatter


    #loop through h(x) values to know which values to highlight 
    for i in range(0,len(h)): 

        #if h(x) > 0
        if ( h[i] > 0):
            
            #add coordinate to sample space
            sp_x.append(x[i,0])
            sp_y.append(x[i,1])
            
            #add g value to g sample space values
            sp_g.append(g[i])

        else:#not apart of sample space

            #add coordinate to sample space
            nonsp_x.append(x[i,0])
            nonsp_y.append(x[i,1])
            
            #add g value to g sample space values
            nonsp_g.append(g[i])

    #scatter plot setup
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Scatter Plot of Random Samples for Monte Carlo Integration with g(x) Sample Space Values Highlighted Red')

    #plot sample space values 
    ax.scatter(sp_x, sp_y, sp_g, zdir= 'z',s=20, c='r')
    
    #plot non sample space values 
    ax.scatter(nonsp_x, nonsp_y, nonsp_g, zdir = 'z', s=20, c='b') 

    #show plot
    plt.show()

def my_Monte_Carlo(x):

        #calculate the g and h values 
        h = my_h_function(x)
        g = my_g_function(x)

        output = 0

        # loop through all of the sample space values 
        for i in range(0, (len(h) - 1) ): 

            #if h_val is greater than zero  
            if ( h[i] > 0):

                #add it's g value to summation
                output = output + g[i]

        # take summation value time |S|/N
        output = output / len(x)

        return output

def my_Monte_Carlo_forCircle(x):

        #calculate the g and h values 
        h = my_h2_function(x)
        g = 1

        output = 0

        # loop through all of the sample space values 
        for i in range(0, (len(h) - 1) ): 

            #if h_val is less than 1 
            if ( h[i] < 1):

                #add it's g value to summation
                output = output + g

        # take summation value time |S|/N
        output = (4 * output )  / len(x) 

        return output

#Exercise (MAIN)

#1
x = np.random.rand(1000,2) # a vector of N two - dimensionalcoordinates in the range [0,1]^2

#2
plot_scatter(x)

#3
Z= my_Monte_Carlo(x)
print("Estimation of I using monte carlo method: ", Z)

#4
X = my_Monte_Carlo_forCircle(x)
print("Estimation of pi using monte carlo method: ", X)

#5

#a: Taking mean and standard deviation of I for N = 1000
I = np.array([])


#run monte carlo method 500 times 
for i in range(0, 500):
    
    #draw a new set of 1000 random coordinate [0,1]^2
    randNum = np.random.rand(1000, 2) 

    #computer monte carlo method and add it to numpy array for taking mean and standard deviation later
    I = np.append(I, my_Monte_Carlo(randNum) )
i
#take mean and standard deviation of I
mean = np.mean(I)
stdev = np.std(I)
print("Mean of random variable I: ", mean)
print("Standard deviation of random variable I: ", stdev)

#b Repeating a but for rand of N

#creating a log scale of N values into a numpy array 
Nset = np.round(np.logspace(1,5,10))

#converting all floats to int
Nset = Nset.astype(int)


#arrays to hold, I values, stdevs, and means
I = np.zeros(shape=(10,500), dtype=int)
I_means = np.zeros(500, dtype=int)
I_stdev = np.zeros(500, dtype=int)

#looping through N set to compute I, means, and std dev
for i in range(10):

    # run monte carlo method 500 times with N random variables
    for trial in range(500):

        #create N random 
        randNum = np.random.rand(Nset[i], 2)

        #append I value to list
        I[i,trial] = my_Monte_Carlo(randNum) 
    
    #calculate means and standard deviations
    I_means[i] = np.mean( I[i,:] )
    I_stdev[i] = np.std( I[i,:] )
    

plt.figure(1)
plt.semilogx(Nset, I[:,0], 'kx')
#plt.semilogx(Nset, n, 'b', label = 'mean')
#plt.semilogx(Nset, np.mean + np.std(I,1), 'r', label = 'mean +/- std')
#plt.semilogx(Nset, np.mean(I) - np.std(I,1), 'r')
plt.xlabel('number of samples')
plt.ylabel('estimated integral')
plt.show()
#6
