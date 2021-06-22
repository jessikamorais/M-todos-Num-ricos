import numpy as np

def rk4( f, t0, tf,x0, h =0.001):
    n = int((tf -t0)/h + 1)
    nx = len(x0)
    x = np.array( [ x0 ] * n )
    
    t = np.linspace( t0, tf, n )

    k1 = np.zeros(nx, dtype = float) 
    k2 = np.zeros(nx, dtype = float) 
    k3 = np.zeros(nx, dtype = float) 
    k4 = np.zeros(nx, dtype = float) 
    xnew = np.zeros(nx, dtype = float)

    for i in range( n - 1 ):
        xnew =[x[i,j] for j in range(nx)]
        k1 = np.multiply(h ,f( xnew, t[i] ))
        xnew =[x[i,j]+0.5*k1[j] for j in range(nx)]
        k2 = np.multiply(h ,f( xnew, t[i] + 0.5 * h ))
        xnew =[x[i,j]+0.5*k2[j] for j in range(nx)]
        k3 = np.multiply(h ,f( xnew, t[i] + 0.5 * h ))
        xnew =[x[i,j]+ k3[j] for j in range(nx)]
        k4 = np.multiply(h ,f(xnew, t[i+1] ))

        for j in range(nx):
            x[i+1,j] = x[i,j] + ( k1[j] + 2.0 * ( k2[j]  + k3[j]  ) + k4[j]  ) / 6.0

    return t,x
