import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def readData(filename):# reading csv file function
    df=pd.read_csv(filename)
    return df.values

x=readData('Linear_X_Train.csv ')
x=x.reshape((3750,))
y=readData('Linear_Y_Train.csv ')
y=y.reshape((3750,))
x=(x-x.mean())/x.std()
def hypo(theta,x):#y=mx+c
    return theta[0]+theta[1]*x


def error(x,y,theta):#computing error
    m=x.shape[0]
    t_err=0
    for i in range(m):
        t_err+=(y[i]-hypo(theta,x[i]))**2

    return 0.5*t_err 
def gradient(x,y,theta):#finding the derivative
    grad=np.array([0.0,0.0])
    m=x.shape[0]
    for i in range(m):
        grad[0]+=(hypo(theta,x[i])-y[i])
        grad[1]+=(hypo(theta,x[i])-y[i])*x[i]   

    return grad 

def gradient_des(x,y,l_r,maxIter):#updating the value f theta suitably to decrease the error
    theta=np.array([0.0,0.0])
    err=[]
    for i in range(maxIter):
        grad=gradient(x,y,theta)
        ce=error(x,y,theta)
        theta[0]=theta[0]-l_r*grad[0]
        theta[1]=theta[1]-l_r*grad[1]
        err.append(ce)
    return theta,err                   

theta,err=gradient_des(x,y,l_r=0.0003,maxIter=20)
print(theta[0],theta[1])

plt.scatter(x,y,color='g')
plt.plot(x,hypo(theta,x),color='r')
plt.show()






