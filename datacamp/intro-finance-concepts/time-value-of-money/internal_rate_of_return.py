import numpy as np
import numpy_financial as npf

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-1000, 200, 250, 300, 350, 400, 450, 500, 550, 600])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-1000, 150, 225, 300, 375, 425, 500, 575, 600, 625])

# Scale the original objects by 1000x
cf_project1 = cf_project_1 * 1000
cf_project2 = cf_project_2 * 1000

# Calculate the internal rate of return for Project 1
irr_project1 = npf.irr(cf_project1)
print("Project 1 IRR: " + str(round(100 * irr_project1, 2)) + "%")

# Calculate the internal rate of return for Project 2
irr_project2 = npf.irr(cf_project2)
print("Project 2 IRR: " + str(round(100 * irr_project2, 2)) + "%")
