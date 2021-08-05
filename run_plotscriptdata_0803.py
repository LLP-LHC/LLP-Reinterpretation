import os
import numpy as np
import math

mX    = np.linspace(250, 3000, 20)
lam   = np.linspace(0.01, 0.01, 1) 

output_dir="/storage/af/user/jmina/Plots/Daniel_Plots/Fig5/Plot3_Data_0803/"
mg5_dir = "/storage/af/user/jmina/LLP-Reinterpretation/MG5_aMC_v2_7_3/bin/mg5_aMC"

for m in mX:
	for l in lam:
		output = output_dir + "m" + str(math.trunc(round(m, 2) * 100)) +"_l"+ str(math.trunc(l * 1000)) + '.dat'
		os.system(mg5_dir + " " + output)
