import pytest
from mat import *

@pytest.mark.parametrize("a, b, result", [([[5,1,2,3],[4,5,9,5],[0,3,6,8]], [[7,8,0,0],[2,1,3,9],[5,6,0,1]], [[12,9,2,3],[6,6,12,14],[5,9,6,9]])])
def test_mat_add(a, b, result):
    assert mat_add(a, b) == result

@pytest.mark.parametrize("a, b, result", [([[7,8,0,0],[2,1,3,9],[5,6,0,1]], [[4,4,0,1],[1,2,6,0],[7,6,7,3]], [[3,4,0,-1],[1,-1,-3,9],[-2,0,-7,-2]])])
def test_mat_subtr(a, b, result):
    assert mat_subtr(a, b) == result

@pytest.mark.parametrize("a, result", [([[5,1,2,3],[4,5,9,5],[0,3,6,8]], [[5,4,0],[1,5,3],[2,9,6],[3,5,8]])])
def test_mat_transp(a, result):
    assert mat_transp(a) == result

@pytest.mark.parametrize("a, b, result", [([[5,1,2,3],[4,5,9,5],[0,3,6,8]], [[7,8,0,0],[2,1,3,9],[5,6,0,1],[4,2,6,3]], [[29,28,20,24],[41,40,32,36],[35,34,26,30]])])
def test_mat_multiply(a, b, result):
    assert mat_multiply(a, b) == result

@pytest.mark.parametrize("a, b, result", [([[4,4,0,1],[1,2,6,0],[7,6,7,3]], 3, [[12,12,0,3],[3,6,18,0],[21,18,21,9]])])
def test_mat_scal(a, b, result):
    assert mat_scal(a, b) == result

@pytest.mark.parametrize("a, b, result", [([[7,8,0,0],[2,1,3,9],[5,6,0,1],[4,2,6,3]], 1, [2,1,3,9])])
def test_mat_str_index(a, b, result):
    assert mat_str_index(a, b) == result

@pytest.mark.parametrize("a, b, result", [([[5,1,2,3],[4,5,9,5],[0,3,6,8]], 1, [1,5,3])])
def test_mat_col_index(a,b, result):
    assert mat_col_index(a,b) == result

@pytest.mark.parametrize("a, b, c, result", [([[4,4,0,1],[1,2,6,0],[7,6,7,3]], 0, 2, [[7,6,7,3],[1,2,6,0],[4,4,0,1]])])
def test_str_swap(a, b, c, result):
    assert str_swap(a, b, c) == result
    
@pytest.mark.parametrize("a, b, c, result", [([[7,8,0,0],[2,1,3,9],[5,6,0,1],[4,2,6,3]], 2, 3, [[7,8,0,0],[2,1,3,9],[15,18,0,3],[4,2,6,3]])])
def test_ind_str_multiply(a, b, c, result):
    assert ind_str_multiply(a, b, c) == result

@pytest.mark.parametrize("a, b, c, d, result", [([[4,4,0,1],[1,2,6,0],[7,6,7,3]], 0, 2, 4, [[4,4,0,1],[1,2,6,0],[23,22,7,7]])])
def test_mat_add_num(a, b, c, d, result):
    assert mat_add_num(a, b, c, d) == result
