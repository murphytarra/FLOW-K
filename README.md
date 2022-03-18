# FLOW-K
Final Year Physics project which investigates transport properties of devices subject to an external electromagnetic field


## Tutorial: Double Quantum Dot

## Initialization 

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
Coupling =[200]
m_max = 50
m = 1000 
E_to_scan = [10]
```
