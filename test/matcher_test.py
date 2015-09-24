from matcher import Match
import pytest

__author__ = 'johannes'


@Match
def func(a: 5, b):
    return 0


@Match
def func(a, b: 5):
    return 1


@Match
def func(a: 6, b: 6):
    return 2


@Match
def func(a, b: 7):
    return 4


@Match
def func(a: 7, b):
    return 5


@Match
def func(a, b):
    return 3


@Match
def no_match_func(a: 1):
    return 6


@Match
def expr_func(a: 'a < 3'):
    return 3


@Match
def expr_func(a: 'a > 4'):
    return 4


@Match
def expr_func(a: 'a == 3'):
    return 5


@Match
def expr_func(a):
    return 6


@Match
def syntax_error_func(a: 'a <!> 2'):
    return 1


@Match
def multi_var_expr_func(a: 'a > b', b):
    return 0


@Match
def multi_var_expr_func(a: 'a <= b', b):
    return 1


def test_matcher():
    assert(func(5, 3) == 0)
    assert(func(3, 5) == 1)
    assert(func(5, 5) == 0)
    assert(func(6, 6) == 2)
    assert(func(1, 2) == 3)


def test_kwargs():
    assert(func(a=5, b=2) == 0)
    assert(func(2, b=5) == 1)
    assert(func(a=3, b=5) == 1)
    assert(func(b=5, a=2) == 1)
    assert(func(b=6, a=6) == 2)
    assert(func(b=5, a=5) == 0)


def test_order():
    assert(func(a=7, b=7) == 4)
    assert(func(b=7, a=7) == 4)
    assert(func(7, 7) == 4)
    assert(func(7, b=7) == 4)


def test_no_match():
    with pytest.raises(TypeError):
        no_match_func(7)
    assert(no_match_func(1) == 6)


def test_expressions():
    assert(expr_func(1) == 3)
    assert(expr_func(5) == 4)
    assert(expr_func(3) == 5)
    assert(expr_func(4) == 6)


def test_expressions_with_all_parameters():
    assert(multi_var_expr_func(2, 1) == 0)
    assert(multi_var_expr_func(1, 1) == 1)
    assert(multi_var_expr_func(1, 2) == 1)


def test_syntax_error_expressions():
    with pytest.raises(SyntaxError):
        syntax_error_func(1)
