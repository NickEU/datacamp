from weighted_avg_cost_of_capital import npv_project1, npv_project2, wacc
from internal_rate_of_return import cf_project1, cf_project2
import numpy_financial as npf

# Calculate the EAA for Project 1
eaa_project1 = npf.pmt(rate=wacc, nper=len(cf_project1), pv=-npv_project1, fv=0)
print("Project 1 EAA: " + str(round(eaa_project1, 2)))

# Calculate the EAA for Project 2
eaa_project2 = npf.pmt(rate=wacc, nper=len(cf_project2), pv=-npv_project2, fv=0)
print("Project 2 EAA: " + str(round(eaa_project2, 2)))
