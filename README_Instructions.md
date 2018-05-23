# README: Code instructions 

## Solving the Schrödinger equation for your own potential. 
This code has been developed to be run using `Jupyter Notebook`. To correctly run the code to solve the Schrödinger equation for 
an arbitrary potential you choose you should open `general_main.ipynb` from the notebook. You will see there are some different blocks. 
You should only modify the initial block which includes all the parameters to set the potential and other constant values. 

### Integration limits
`rmin` and `rmax` correspond to the integration limits of the integration. You may have to change them depending on the potential 
you are working with.

### Defining the potential
You should define the potential you want to use by using the original form but changin `x` to `x = rmin + h·i`. 

### Eigenvalues
You can determine the error and the number of iterations used to obtain the eigenvalues. As well you can determine which eigenvalues 
should be found by setting the first eigenvalue `n1` you want to obtain and the last one `n2`.

### Simulation
- `c0`, `c1`, `c2` and `c3` correspond to the coefficients of the different first four eigenstates from which is conformed the state which is 
simulated.
- w correspond to the frequency of the simulation.

Once every parameter is set you can run all the blocks and you will obtain the different outputs: Eigenvalues, Eigenstates and a simulation of the probability density temporal evolution.

**Please, DO NOT MODIFY other blocks than this first setting block.** Modifications in other blocks would imply changing the inner structure of the code
and may trigger malfunctions.

***

## Other codes
As well the Github includes a series of codes which include:
1) The codes which were used to prove the robustness and accuarcy of the numerical methods, using the Poschl-Teller potential (`PoschlTeller.ipynb`). 
You can access them freely and run them to obtain the results in question. Please, do not modify this codes. 

2) The codes which were used to solve the hyfrogen atom model and obtain the different components of the probability density function (`main_3d.ipynb`). 
In this case, the first block allows to modify the values of the quantic numbers to decide which probability density function is going to be obtained.
**Please, DO NOT MODIFY other blocks than this first setting block.**

3) The rest of the codes correspond to the different numerical methods used along all the applications developed. All of them are 
accurately comented to ensure a good understanding of the codes for an external user in case it was to modify or change any section of it, 
