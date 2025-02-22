import sys
sys.path.append('../src')
import elastoplastic_model as ep
import numpy as np
import pytest

@pytest.fixture
def ElastoMaterial():
    E=1000
    E_t=100
    Y0=10
    H=E*E_t/(E-E_t)
    return ep.ElastoPlastic(E=E,H=H,Y0=Y0)

@pytest.fixture
def IsoMaterial():
    E=1000
    E_t=100
    Y0=10
    H=E*E_t/(E-E_t)
    return ep.IsotropicHardening(E=E,H=H,Y0=Y0)


@pytest.fixture
def KinMaterial():
    E=1000
    E_t=100
    Y0=10
    H=E*E_t/(E-E_t)
    return ep.KinematicHardening(E=E,H=H,Y0=Y0)

def test_start_experiment_kinematic():
    E=1000
    E_t=100
    Y_0=10
    H=E*E_t/(E-E_t)

    strain_1 = np.linspace(0,0.05,1000)
    strain_2 = np.linspace(0.05,-0.05,2000)
    strain_3 = np.linspace(-0.05,0.075,2500)
    strain_4 = np.linspace(0.075,-0.025,2000)
    strain_list=np.concatenate((strain_1,strain_2,strain_3,strain_4),axis=0)

    kin = ep.KinematicHardening(E=E,H=H,Y_0=Y_0)
    stress_list = kin.start_experiment(strain_list)
    print(stress_list)  

def test_start_experiment_iso_0():
    E=1000
    E_t=100
    Y0=10
    H=E*E_t/(E-E_t)
    strain_list=[0.001,0.002,0.003]
    iso = ep.IsotropicHardening(E=E,H=H,Y_0=Y0)
    found = iso.start_experiment(strain_list)
    print(found)  

def test_start_experiment_iso_1():
    E=2000
    E_t=200
    Y0=20
    H=E*E_t/(E-E_t)
    strain_list=[0.002,0.004,0.006]
    iso = ep.IsotropicHardening(E=E,H=H,Y_0=Y0)
    found = iso.start_experiment(strain_list)
    print(found)  

def run_tests():
    test_start_experiment_kinematic()
    test_start_experiment_iso_0()
    test_start_experiment_iso_1()

run_tests()