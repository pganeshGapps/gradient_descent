from numpy import *
import matplotlib.pyplot as plt

DRAWING_ERROR_GRAPH=False
# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_a_line(b, m, points):
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
    
    xis=list(range(-10,100))
    if not DRAWING_ERROR_GRAPH:
        #initial line
        yis=list([m*x+b for x in xis])
        plt.plot(xis,yis,color='b',linewidth=3,label="initial")#,label=str(i))
     
    delta_ls=[]
    for i in range(num_iterations):
        prev_error=compute_error_for_a_line(b, m, points)
        b, m = step_gradient(b, m, array(points), learning_rate)
        new_error=compute_error_for_a_line(b, m, points)
        delta=abs(new_error-prev_error)
        delta_ls.append(delta)
#        if delta< 0.0001:
#            print("Delta={0}, iterations={1}".format(delta,i))
#            break
        #print(delta,end="\t")
        if not DRAWING_ERROR_GRAPH:
            yis=list([m*x+b for x in xis])
            plt.plot(xis,yis)
        #time.sleep(0.1)
        #plt.draw()
    
    #ls=array(ls)
    #plt.scatter(ls[:,1],ls[:,0])
    
    if not DRAWING_ERROR_GRAPH:
        #final line
        yis=list([(m*x+b) for x in xis])
        plt.plot(xis,yis,color="g",linewidth=3,label="final")#,label=str(i))
        plt.xlabel('x_data', fontsize=18)
        plt.ylabel('y_data', fontsize=16)
    else:
        plt.plot(list(range(len(delta_ls))),delta_ls)
        plt.xlabel('iteration', fontsize=18)
        plt.ylabel('MSE', fontsize=16)
    #print(*delta_ls[275:290])
    print("Runner completed its job.\nDelta={0}, iterations={1}".format(delta,num_iterations))
    return [b, m]

def run():
    points = genfromtxt("data.csv", delimiter=",")
    if not DRAWING_ERROR_GRAPH:
        plt.scatter(points[:,0],points[:,1])
    learning_rate = 0.00005
    initial_b =0#0 # initial y-intercept guess
    initial_m =4.1#0 # initial slope guess
    num_iterations = 270
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_a_line(initial_b, initial_m, points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_a_line(b, m, points)))
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    run()
