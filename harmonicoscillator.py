import time

class HarmonicOscillator():
    def __init__(self, m, k, v, x):
        self.m = m
        self.k = k
        self.v = v
        self.x = x

    def step(self, timestep):
        #v1 = v0 + a*dt
        self.v = self.v - (self.k/self.m)*self.x*timestep
        self.x = self.x+self.v*timestep

    def printPosition(self):
        fraction = self.x / 5
        #hamiltonian should not vary for a harmonic oscillator (it is time independent). Variation indicates discretization error. 
        #for some reason reducing the mass also increases the error on the Hamiltonian -- does discretization error
        #increase for low mass (larger acceleration)??
        kineticEnergy = self.m*self.m*self.v*self.v/(2*self.m)
        potentialEnergy = 0.5*self.k*self.x**2
        hamiltonian = kineticEnergy + potentialEnergy
        print('|' + ' '*(round(30-30*fraction)) + '*' + ' '*(round(30+30*fraction)) + '|' + "Hamiltonian="+str(round(hamiltonian, 5))+" KE="+str(round(kineticEnergy, 2))+" PE="+str(round(potentialEnergy, 2)), end='\r')    
#        print(hamiltonian, end='\r')

#input: m, k, v, initial position)
particle = HarmonicOscillator(2, 2, 0, 5)

for i in range(1000000):
    particle.step(0.0001)
    if i%1000:
        particle.printPosition()
    time.sleep(0.00005)

