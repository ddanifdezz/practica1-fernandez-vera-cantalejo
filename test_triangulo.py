import pytest 
from triangulo import check_triangle

def test_case1():
    assert check_triangle(6, 5, 10) == "Triangulo escaleno"

def test_case2():
    assert check_triangle(3, 3, 4) == "Triangulo isosceles"

def test_case3():
    assert check_triangle(6, 6, 6) == "Triangulo equilatero"

def test_case4():
    assert check_triangle(4, 3, 0) == "No es un triangulo"

def test_case5():
    assert check_triangle(8, 2, 4) == "No es un triangulo"

