import numpy as np
import pytest

from regression import LinearRegression as SingleLinearRegression


@pytest.fixture(scope='module')
def reg_model(single_linear_regression_data):
    linear_regression_model = SingleLinearRegression(independent_vars=single_linear_regression_data['independent_vars'],
                                                     dependent_var=single_linear_regression_data['dependent_var'],
                                                     learning_rate=0.01,
                                                     train_split=0.7,
                                                     seed=123)
    return linear_regression_model


def test_single_linear_regression_data_passing_correctly(reg_model, single_linear_regression_data):
    """
    Setup linear regression model
    :return:
    """
    #assert(reg_model.independent_vars_train.all() == single_linear_regression_data['independent_vars'].all())
    #assert(reg_model.dependent_var.all() == single_linear_regression_data['dependent_var'].all())
    assert(type(reg_model.independent_vars_train) == np.ndarray)
    assert(type(reg_model.dependent_var_train) == np.ndarray)


def test_single_linear_regression_fit(reg_model):
    """
    Test regression model coefficients
    :return:
    """
    assert(pytest.approx(reg_model.b1, 0.01) == 1.24)
    assert(pytest.approx(reg_model.b0, 0.01) == 0.38)


def test_single_linear_regression_rmse(reg_model):
    """
    Test regression model root mean squared error
    :return:
    """
    assert(pytest.approx(reg_model.root_mean_squared_error(), 0.02) == 0.26)


def test_single_linear_regression_r_squared(reg_model):
    """
    Test regression model r_squared
    :return:
    """
    assert(pytest.approx(reg_model.r_squared(), 0.01) == 0.58)
