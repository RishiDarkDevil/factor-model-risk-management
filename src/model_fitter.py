import statsmodels.api as sm

def fit_factor_model(asset_returns, factors):
    X = sm.add_constant(factors)  # Add intercept
    model = sm.OLS(asset_returns, X).fit()
    return model
