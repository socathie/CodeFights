def fareEstimator(t,d,minu,mile):
    return [t*i+d*j for (i,j) in zip(minu,mile)]
