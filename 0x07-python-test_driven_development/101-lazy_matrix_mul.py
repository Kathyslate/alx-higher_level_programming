#!/usr/bin/python3
"""Module for function lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.
    
    Parameters:
    m_a (list of lists or 2D NumPy array): First matrix.
    m_b (list of lists or 2D NumPy array): Second matrix.
    
    Returns:
    2D NumPy array: Result of the multiplication.
    
    Raises:
    LazyMatrixMulError: If the matrices cannot be multiplied.
    """
    return numpy.matmul(m_a, m_b)
