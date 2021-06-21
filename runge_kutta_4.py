import numpy as np

def rk4( f, t0, tf,x0, h =0.001): 

    n = int((tf -t0)/h + 1) 
    x = np.array( [ x0 ] * n )
    t = np.linspace( t0, tf, n )

    for i in range( n - 1 ):
        k1 = h * f( x[i], t[i] )
        k2 = h * f( x[i] + 0.5 * k1, t[i] + 0.5 * h )
        k3 = h * f( x[i] + 0.5 * k2, t[i] + 0.5 * h )
        k4 = h * f( x[i] + k3, t[i+1] )
        x[i+1] = x[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    
    return t,x
