import numpy as np
from asset_returns import asset_returns_before, asset_returns_during

asset_returns = [asset_returns_before, asset_returns_during]
weights = [0.25, 0.25, 0.25, 0.25]

# Create portfolio returns for the two sub-periods using the list of asset returns
portfolio_returns = np.array([x.dot(weights) for x in asset_returns])

# Derive portfolio losses from portfolio returns
losses = - portfolio_returns

# Find the historical simulated VaR estimates
VaR_95 = [np.quantile(x, 0.95) for x in losses]

# Display the VaR estimates
print("VaR_95, 2005-2006: ", VaR_95[0], '; VaR_95, 2007-2009: ', VaR_95[1])

# Great! As you can see, the VaR estimates are very different for the two time periods.
# This indicates that over the entire 2005 - 2009 period the loss distribution was likely not stationary.
# Historical simulation, while very general,
# should be used with caution when the data is not from a stationary distribution.
