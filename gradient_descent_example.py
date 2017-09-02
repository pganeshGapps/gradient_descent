from numpy import *
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
from matplotlib import style


fig.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add(1,1,1)

X=[]
Y=[]
points=array()

def animate(i):
    xis=X
    yis=Y
    ax1.clear()
    ax1.scatter(points[:,0],points[:,1])
    ax1.plot(xis,yis)
    
# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    len_=len(points)
    for i in range(0, len_):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len_)

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    
    ls=[]
    ls.append([b,m])
    #initial line
#    xis=list(range(-50,141))
#    yis=list([ls[-1][1]*x+ls[-1][0] for x in xis])
#    plt.plot(xis,yis,color='b',linewidth=3)#,label=str(i))
    
    delta_ls=[]
    for i in range(num_iterations):
        prev_error=compute_error_for_line_given_points(b, m, points)
        b, m = step_gradient(b, m, array(points), learning_rate)
        new_error=compute_error_for_line_given_points(b, m, points)
        delta=abs(new_error-prev_error)
        delta_ls.append(delta)
        if delta< 0.0001:
            print("Delta={0}, iterations={1}".format(delta,i))
            break
        #print(delta,end="\t")
#        xis=list(range(-50,141))
#        yis=list([ls[-1][1]*x+ls[-1][0] for x in xis])
#        plt.plot(xis,yis)
        #time.sleep(0.1)
        #plt.draw()
        ls.append([b,m])
    
    #ls=array(ls)
    #plt.scatter(ls[:,1],ls[:,0])
    
    #final line
    xis=list(range(-50,141))
    yis=list([ls[-1][1]*x+ls[-1][0] for x in xis])
    plt.plot(xis,yis,color="g", linewidth=3)#,label=str(i))
    #plt.plot(list(range(len(delta_ls))),delta_ls)
    #print(*delta_ls[275:290])
    return [b, m]

def run():
    points = genfromtxt("data.csv", delimiter=",")
    #plt.scatter(points[:,0],points[:,1])
    learning_rate = 0.00005
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 270
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))
if __name__ == '__main__':
    run()
