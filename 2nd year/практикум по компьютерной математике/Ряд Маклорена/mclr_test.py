import pytest
from mat import *

@pytest.mark.parametrize("a, b, result", [(1, 5, 2.708333333333333)])
def test_exp(a, b, result):
    assert exp(a, b) == result

@pytest.mark.parametrize("a, b, result", [(1, 5, 0.20530450508685372)])
def test_sinx(a, b, result):
    assert sinx(a, b) == result

@pytest.mark.parametrize("a, b, result", [(1, 5, 0.5403025793650793)])
def test_cosx(a, b, result):
    assert cosx(a, b) == result

@pytest.mark.parametrize("a, b, result", [(1, 5, -819345.93)])
def test_arcsinxa(a, b, result):
    assert arcsinx(a, b) == result

@pytest.mark.parametrize("a, b, result", [(1, 5, 819347.5)])
def test_arccosx(a, b, result):
    assert arccosx(a, b) == result