import numpy
from math import sin, cos, pi, log
import matplotlib.pyplot as plt

def plot(vec):
    plt.plot(vec)
    plt.show()

def X(z,phi):
    return z * cos(phi)

def Y(z, phi, sigma):
    a = cos(phi) * (cos(sigma) - 1)
    b = sin(phi) * sin(sigma)
    return z * (a - b)

def z2(z):
    return (1 + pi) * (z**2) / ((1-4*z)**2)

def s1(z, phi, sigma, teta):
    x = X(z, phi)
    y = Y(z, phi, sigma)
    return (y**2) / ((1+x+teta*y)**2)

def s2(z, sigma):
    return z2(z) * (sigma**2)

def test(z = 0.2, jump_phi=10, jump_sigma=10, printout=False):
    res = []
    for teta_int in xrange(0, 11, 1):
        teta = teta_int / 10.
        for phi_int in xrange(0, 628, jump_phi):
            phi = phi_int / 100.
            for sigma_int in xrange(-1256, 1256, jump_sigma):
                sigma = sigma_int / 100.
                tmp_data = s2(z, sigma) - s1(z, phi, sigma, teta)
                res.append(tmp_data)
                if printout:
                    print len(res) - 1, z, sigma, phi, teta, tmp_data
    print log(len(res),2)
    return res

