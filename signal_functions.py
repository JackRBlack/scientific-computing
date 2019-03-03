# Gaussian functions

def gaussian_1D(x, mu, sigma):
    '''
        A gaussian function.
        
        args:
            x : [np.array] variable, e.g. np.linspace(-10, 10, 1000)
            mu : [double] expectation value, e.g. 0.
            sigma : [double] standard deviation, e.g. 1.
        
        return:
            g(x) : [np.array] a gaussian distribution function.
            
        note:
            1. FWHM = 2\sqrt(2*\ln(2))*\sigma = 2.35482 \sigma
            2. Integral = 1
            
    '''
    g = np.exp(-0.5 * (x - mu)**2 / sigma**2) / (sigma * np.sqrt(2*np.pi))
    return g

def gaussian_1D_FWHM(x, mu, FWHM):
    '''
        A gaussian function.
        
        args:
            x : [np.array] variable, e.g. np.linspace(-10, 10, 1000)
            mu : [double] expectation value, e.g. 0.
            FWHM : [double] full width half maximum, e.g. 1.
        
        return:
            g(x) : [np.array] a gaussian distribution function.
            
        note:
            1. FWHM = 2\sqrt(2*\ln(2))*\sigma = 2.35482 \sigma
            2. Integral = 1
            
    '''
    sigma = FWHM / 2.35482
    g = np.exp(-0.5 * (x - mu)**2 / sigma**2) / (sigma * np.sqrt(2*np.pi))
    return g