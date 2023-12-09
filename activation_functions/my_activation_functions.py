"""
    Implementation of different activation functions in Deep Learning 😎
"""
import numpy as np


def linear_function(x: np.ndarray, m=1) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray
        m (int, optional): multiplying factor. Defaults to 1.

    Returns:
        int: product of x and m 
    """
    return x * m


def relu(x: np.ndarray) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray

    Returns:
        np.ndarray: your output ndarray
    """
    return np.maximum(x, 0)


def elu(x: np.ndarray, alpha=0.01) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray
        alpha (int, optional): alpha value. Defaults to 0.01.

    Returns:
        np.ndarray: your output ndarray with Elu (exponential linear unit) applied to it  
    """
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


def leaky_relu(x: np.ndarray, alpha=0.01) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray
        alpha (int, optional): alpha value. Defaults to 0.01.

    Returns:
        np.ndarray: your output ndarray with Leaky ReLU applied to it  
    """
    return np.where(x > 0, x, 0.01 * x)


def sigmoid(x: np.ndarray) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray

    Returns:
        np.ndarray: your output ndarray with Sigmoid applied to it  
    """
    return 1 / (1 + np.exp(-x))


def tanh(x: np.ndarray) -> np.ndarray:
    """_summary_

    Args:
        x (np.ndarray): your input ndarray

    Returns:
        np.ndarray: your output ndarray with Tanh applied to it  
    """
    # return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    return np.tanh(x)
