# FLOW-K

### Please note that this project is still underdevelopment and will be updated on a regular basis.

Here we provide a package which calculates the transport properties of a N dimensional device subject to an external electromagnetic field. 
Using a model developed by Martinez et. al. (see INSERT), a recursive scheme was implemented to calculate the current flowing through an electronic device subject to an electric field when attached to electron resoirvoirs. 

This project was developed as part of a Theoretical Physics Final Year Project at Trinity College Dublin. 

## Features
- Measure the current flowing throughout an electronic device when attached to two electron resoirvoirs
- Investigate transport properties of an electronic device when an external potential is applied
- Determine how current flow through various systems, such as DNA wires is effected by an external potential

## Upcoming Updates
- Tutorial for Quantum Ratchets
- Tutorial for DNA Wire
- Package code such that its easy to download and install

## Tutorial: Double Quantum Dot

First we import in the functions and packages required.

```javascript
from FLOW_K import E_field as E_field
from FLOW_K import Electrons as Electrics
```

Our first step is to define the dimensionality and Hamiltonian of the system we wish to investigate. In this example we will use a double Quantum Dot;

```javascript
Hamiltonian = [[-5, 1], [1, 5]]
```

We normalise all other parameters with regards to the hopping parameter $t$ set all other parameters as follows:


| Name      | Symbol   | Value  |
| :------------- | :----------: | -----------: |
|  Boltzmann Temperature | kT  | 0.25   |
|  Applied Bias | V   | 0   |
|  Self Energy (Leads) | Gamma   | 0.5|
|  Frequency Range of Efield | E_to_scan   | -40 - 0.1   |
| Number of Floquet Modes | m_max | 10  |
| Magnitude of E-field | C | 6 |
| Number of points | m | 200 |
| Dimensionality of Hamiltonian | n | 2 |

```javascript
T = 0.01 
V = 0.0 
Gamma = 0.5
n = 2 
C =[200]
m_max = 50
m = 1000 
E_to_scan = [10]
```

After setting all our parameters, we now create the class which will contain both our external electric field and central electronic system

```javascript
H = Electrons(n, Hamiltonian, V, T);  
E = E_field( -E_to_scan[0], -E_to_scan[-1], E_to_scan, Gamma, C/2, C/2)
```

Our next step is to set up the simulation and determine the current for a range of different frequencies for the external electric field. 
To do so, we use the function `.coupling2` 

```javascript
current = coupling2(E, Hamiltonian, m, m_max) 
```
We can plot the results of the current to visualise the current for a variety of different frequcies

```javascript
plt.plot(E_to_scan, current[0], linestyle="-", linewidth=1, marker = "o", markersize = 0)
plt.ylabel("Normalised Current")
plt.xlabel(" Applied Bias accross Leads [t]")
plt.grid("on")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.style.use('ggplot')
plt.show()
```
