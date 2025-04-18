import numpy as np

def compute_covariance_matrix(betas, factor_cov, residuals_var):
    # betas: (N assets x K factors)
    # factor_cov: (K x K) factor covariance
    # residuals_var: (N x 1) residual variances
    return betas @ factor_cov @ betas.T + np.diag(residuals_var)

def calculate_var(portfolio_weights, cov_matrix, alpha=0.05):
    portfolio_var = portfolio_weights.T @ cov_matrix @ portfolio_weights
    var = np.sqrt(portfolio_var) * 1.645  # 1.645 for 5% VaR assuming normal
    return var
