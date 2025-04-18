def compute_model_metrics(model):
    return {
        "R2_adj": model.rsquared_adj,
        "AIC": model.aic,
        "BIC": model.bic
    }
