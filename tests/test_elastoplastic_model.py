from assignment1 import elastoplastic as ep
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
