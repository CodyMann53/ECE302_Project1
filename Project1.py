from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np
import matplotlib.pyplot as plt


#adding python file path name


#FUNCTIONS
def my_h2_function(x):
    

    output = []
    #loop through all of the vectors
    for cor in x:

        #calculate value for coordinate and then append it to list
        val = math.pow(cor[0], 2) + math.pow(cor[1],2)
        output.append(val)

    return output

def my_h_function(x):

    output = []
    #loop through all of the vectors
    for cor in x:

        #calculate value for coordinate and then append it to list
        val = math.pow(cor[0], 3) + math.pow(cor[1], 2) + 2 * cor[0]*cor[1] - math.sin(cor[0]) + math.cos(2 * math.pi * cor[0] * cor[1] ) - 1
        output.append(val)

    return output

def my_g_function(x):

    output = []
    #loop through all of the vectors
    for cor in x:

        val = (1 / (2 * math.pi) ) * math.exp( -(math.pow(cor[0], 2) + math.pow(cor[1], 2) ) / 2 )
        output.append(val)

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

            #if h_val is greater than zero  
            if ( h[i] < 1):

                #add it's g value to summation
                output = output + g

        # take summation value time |S|/N
        output = (1/4) * (  (output * math.pi) / len(x) )

        return output
#Exercise (MAIN)

#1
x = np.random.rand(1000,2) # a vector of N two - dimensionalcoordinates in the range [0,1]^2

#2
plot_scatter(x)

#3

I = my_Monte_Carlo(x)
print(I)

I = my_Monte_Carlo_forCircle(x)
print(I)
