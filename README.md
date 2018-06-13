# HarmonicOscillator
Toy harmonic oscillator in python, demonstrating the effect of timestep and mass on the Hamiltonian

## notes 
This script demonstrates a few things that might help my understanding of statistical mechanics.
A harmonic oscillator is a single particle, one dimensional system where the force on the particle is proportional to the displacement:
`F = -kx`
with k being the spring constant. 

The script uses a timestep to evolve the particle coordinates, using `v(t) = v0 - a*t`.

## Hamiltonian 
The force is the negative of the derivative of the potential energy i.e. `dU/dx = -F`. So, potential energy is `1/2*k^2x`. 

The kinetic energy is `1/2*mv^2`, and since `v = p / m` we have `KE = p^2 / 2m`.
(https://deutsch.physics.ucsc.edu/6A/book/momentum/node3.html)
Together they make the Hamiltonian. 

## Discretization error
A harmonic oscillator is time-independent, meaning the Hamiltonian should not vary. It does in this simple case. Reducing the timestep reduces the movement of the Hamiltonian - a reduction in error. This is an exampe of discretization error. Large steps = large error and vice versa. Changing the mass has an equivalent effect, which is a neat demonstration of what Feenstra et al mentioned in their Hydrogen Mass Repartitioning paper - scaling the total mass of a system is equivalent to scaling time. 

Feenstra: Improving Efficiency of Large Time-Scale Molecular Dynamics Simulations of Hydrogen-Rich Systems
