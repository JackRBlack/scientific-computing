# This is a module including physical constant.

# The author is Wenjie Chen. Contact me via E-mail: wenjiechen@pku.edu.cn

# Established on Jun 18th, 2018.
# Last edited on Jun 20th, 2018.

# Part 1: physical contant

# Universal constants

c = 299792458 # <c> [m s^-1] {defined} <the speed of light in vacuum>

G = 6.67408e-11 # <G> [m^3 kg^-1 s^-2] {4.7e-5} <Newtonian constant of gravitation>

h = 6.626070040e-34 # <h> [J s] {1.2e-8} <Planck constant>

hbar = 1.054571800e-34 # <\hbar> [J s] {1.2e-8} <reduced Planck constant, hbar = h/(2*pi)>

# Electromagnetic constants

mu_0 = 1.256637061e-6 # <\mu_0> [N A^-2] {defined} <magnetic constant (vacuum permeability), defined to be 4*pi*1e-7>

e_0 = 8.854187817e-12 # <\epsilon_0> [F m^-1] {defined} <electric constant (vacuum permittivity), defined to be 1/(mu_0*c^2)>

k_e = 8.9875517873681764e9 # <k_e> [kg m^3 s^-4 A^-2] {defined} <Coulomb's constant, defined to be 1/(4*pi*e_0)>

e = 1.6021766208e-19 # <e> [C] {6.1e-9} <elementary charge>

# Atomic and nuclear constants

a = 7.2973525664e-3 # <\alpha> [] {2.3e-10} <fine-structure constant, defined to be e^2/(4*pi*e_0*hbar*c)>

m_e = 9.10938356e-31 # <m_e> [kg] {1.2e-8} <electron mass>

m_p = 1.672621898e-27 # <m_e> [kg] {1.2e-8} <proton mass>

a_0 = 5.2917721067e-11 # <a_0> [m] {2.3e-9} <Bohr radius, defined to be hbar/(a*m_e*c)>

r_e = 2.8179403227e-15 # <r_e> [m] {6.8e-10} <classical electron radius, defined to be e^2/(4*pi*e_0*m_e*c^2)>

# Physico-chemical constants

N_A = 6.022140858e23 # <N_A> [mol^-1] {1.2e-8} <Avogadro constant>

k_B = 1.38064853e-23 # <k_B> [J K^-1] {5.7e-7} <Boltzmann constant>

R = 8.3144598 # <R> [J mol^-1 K^-1] {5.7e-7} <gas constant, R = N_A * k_B>

m_u = 1.660539040e-27 # <m_u> [kg] {1.2e-8} <atomic mass constant>

# Adopted values

g_n = 9.80665 # <g_n> [m s^-2] {defined} <standard acceleration of gravity>

atm = 101325 # <atm> [Pa] {defined} <standard atmosphere>

# Quantum Hall effect

quan_r = 25812.80745 # <> [ohm] <quantum resistivity, 2*pi*hbar/e^2>

flux_quan = 4.135667662e-15 # <\phi_0> [Wb] <flux quantum, 2*pi*hbar/e>


# Part 2: unit conversion

# Temperature

def C_2_F(varA):
    '''
        Convert Celsius to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = C_2_F(26.5)
    '''
    
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA * 1.8 + 32
    return varB

def F_2_C(varA):
    '''
        Convert Fahrenheit to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = F_2_C(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8
    return varB

def C_2_K(varA):
    '''
        Convert Celsius to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Celsius.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = C_2_K(26.5)
    '''
    if varA < -273.15:
        raise ValueError('Temperature cannot be lower than -273.15 °C (0 K)!')
    varB = varA + 273.15
    return varB

def K_2_C(varA):
    '''
        Convert Kelvin to Celsius.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Celsius.
            
        example:
            T_C = K_2_C(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = varA - 273.15
    return varB

def F_2_K(varA):
    '''
        Convert Fahrenheit to Kelvin.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Fahrenheit.
            
        returns:
            varB : [double] A value in Kelvin.
            
        example:
            T_K = F_2_K(40.5)
    '''
    
    if varA < -459.67:
        raise ValueError('Temperature cannot be lower than -459.67 °F (0 K)!')
    varB = (varA - 32) / 1.8 + 273.15
    return varB

def K_2_F(varA):
    '''
        Convert Kelvin to Fahrenheit.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in Kelvin.
            
        returns:
            varB : [double] A value in Fahrenheit.
            
        example:
            T_F = K_2_F(0)
    '''
    if varA < 0:
        raise ValueError('Temperature cannot be lower than 0 K!')
    varB = (varA - 273.15) * 1.8 + 32
    return varB

# Energy

def J_2_eV(varA):
    '''
        Convert joule to electronvolt.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in joule.
            
        returns:
            varB : [double] A value in electronvolt.
            
        example:
            E_eV = J_2_eV(5.0)
    '''
    varB = varA / e
    return varB

def eV_2_J(varA):
    '''
        Convert electronvolt to joule.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in electronvolt.
            
        returns:
            varB : [double] A value in joule.
            
        example:
            E_J = eV_2_J(1.0)
    '''
    varB = varA * e
    return varB

def J_2_K(varA):
    '''
        Convert joule to kelvin using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in joule.
            
        returns:
            varB : [double] A value in kelvin.
            
        example:
            T = J_2_K(5.0)
    '''
    varB = varA / k_B
    return varB

def K_2_J(varA):
    '''
        Convert kelvin to joule using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in kelvin.
            
        returns:
            varB : [double] A value in joule.
            
        example:
            E = K_2_J(5.0)
    '''
    varB = varA * k_B
    return varB

def eV_2_K(varA):
    '''
        Convert electronvolt to kelvin using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in eV.
            
        returns:
            varB : [double] A value in kelvin.
            
        example:
            T = eV_2_K(1.0)
    '''
    varB = eV_2_J(varA) / k_B
    return varB

def K_2_eV(varA):
    '''
        Convert kelvin to electronvolt using Boltzmann constant.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in kelvin.
            
        returns:
            varB : [double] A value in electronvolt.
            
        example:
            T = K_2_eV(23.0)
    '''
    varB = J_2_eV(varA * k_B)
    return varB

# Pressure

def Pa_2_bar(varA):
    '''
        Convert pascal to bar.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in bar.
            
        example:
            P_bar = Pa_2_bar(12345.6)
    '''
    varB = varA / 1e5
    return varB

def bar_2_Pa(varA):
    '''
        Convert bar to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in bar.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = bar_2_Pa(1.0)
    '''
    varB = varA * 1e5
    return varB

def Pa_2_atm(varA):
    '''
        Convert pascal to standard atomsphere.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in atm.
            
        example:
            P_atm = Pa_2_atm(12345.6)
    '''
    varB = varA / atm
    return varB

def atm_2_Pa(varA):
    '''
        Convert standard atomsphere to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in atm.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = atm_2_Pa(1.0)
    '''
    varB = varA * atm
    return varB

def Pa_2_Torr(varA):
    '''
        Convert pascal to torr.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in pascal.
            
        returns:
            varB : [double] A value in torr.
            
        example:
            P_Torr = Pa_2_Torr(12345.6)
    '''
    varB = varA * 760 / atm
    return varB

def Torr_2_Pa(varA):
    '''
        Convert torr to pascal.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            varA : [double] A value in torr.
            
        returns:
            varB : [double] A value in pascal.
            
        example:
            P_Pa = Torr_2_Pa(1.0)
    '''
    varB = varA * atm / 760
    return varB

