# A numerical approach to solving Schrödinger equation.

Quantum Mechanics is considered as one of the most weird branches in physics with the most, although accurate, counterintuitive predictions. The problem lies not on the theory but on what it is trying to explain: the microscopic world. Moreover, due to the complicated form of the Schrödinger equation, there are only few examples where it exists an analytical solution to the problem. 

Therefore, the motivation of this repository is to explore the incredible effects of Quantum Mechanics solving the Schrödinger equation numerically under different potentials. The programs allows to obtain the eigenvalues, eigenstates and a temporal evolution of the probability density of a particle for the potential introduced by the user.

As for the numerical system precision, the method has been stressed to find out its precision and the method is used for two real models: the ammonia molecule and the hydrogen atom. 

This repository offers the open-source `python 2.7` programs to solve the Schrödinger equation under arbitrary potentials. It is designed to be implemented through `Jupiter Notebook`, to ease user's experience and facilitate working with arbitrary potentials.

 https://gmegh.github.io/quantumschrod/


## Working with `Jupyter Notebook`

Download the programs as a zip and install `Jupyter Notebook`. Then run the `general_potential.py` and introduce the arbitrary potential with which you want to work. Remind that the only block which has to be modified is the first one. Should you were to modify deeper code or other blocks, this may trigger malfunctions to the program.


## Precision and Robustness
The Richardson method used in calculating the eigenvalues, ensures a rapid, robust and accurate results. Furthermore, the program has been numerically stressed out with different high-dificulty potentials, such as the Poschl-Teller modified potential,

## Real-case applications
### Ammonia molecule

### Hydrogen Atom
Furthermore, it is also presented a real-case application, which allows to study the radial wave-fucntion of the Hydrogen atom, through the three-dimensional case. The angular wave-function is also obtained thorugh the analytic expression and is represented in a polar plot and 3D to show the shape of electron orbitals in H atom, for an arbitrary value of the azimuthal quantum number l. 



