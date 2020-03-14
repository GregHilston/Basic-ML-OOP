import pytest
import pandas as pd
import numpy as np


@pytest.fixture(scope='session')
def single_linear_regression_data() -> dict:
    """
    Setup test data for
    :return:
    """
    df = np.array(pd.read_csv('my_test_data/my_test_data.csv'))
    yield {
        'dependent_var': df[:, 3],
        'independent_vars': df[:, 2]
    }
    return print('single_linear_regression_data fixture finished.')


@pytest.fixture(scope='session')
def multiple_linear_regression_data() -> dict:
    """
    Setup test data for
    :return:
    """
    df = np.array(pd.read_csv('my_test_data/my_test_data.csv'))
    yield {
        'dependent_var': df[:, 3],
        'independent_vars': df[:, 0:2]
    }
    return print('multiple_linear_regression_data fixture finished.')
