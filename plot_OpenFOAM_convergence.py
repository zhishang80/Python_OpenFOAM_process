#!/usr/bin/python
# -*- coding: <encoding name> -*-

import os
import sys
import math

residuals_file = "log"

if not os.path.isfile(residuals_file):
	print "log.Foam file not found at "+residuals_file
	print "Be sure that the case has been run and you have the right directory!"
	print "Exiting."
	sys.exit()

outfile_Time = open("timeStep",'w')
outfile_CoMax = open("MaxCo",'w')

outfile_Ux_1st = open("Ux_1st_residual",'w')
outfile_Ux_2nd = open("Ux_2nd_residual",'w')
outfile_Uy_1st = open("Uy_1st_residual",'w')
outfile_Uy_2nd = open("Uy_2nd_residual",'w')
outfile_Uz_1st = open("Uz_1st_residual",'w')
outfile_Uz_2nd = open("Uz_2nd_residual",'w')

outfile_p_1st = open("p_1st_residual",'w')
outfile_p_2nd = open("p_2nd_residual",'w')

outfile_k = open("k_residual",'w')
outfile_Epsilon = open("epsilon_residual",'w')

i_Ux = 0
i_Uy = 0
i_Uz = 0
i_p = 0

with open(residuals_file,"r") as datafile:
	for line in datafile:
		if line.startswith("Time = "):
			timeStep = line.split(' ')[2]
			outfile_Time.write(timeStep)
		elif line.startswith("Courant Number"):
			CourantNo = line.split(' ')[5]
			outfile_CoMax.write(CourantNo)
		elif line.startswith("smoothSolver:  Solving for Ux"):
			if i_Ux == 0:
				str_Ux=line.split(' ')[8]
				res_Ux=str_Ux.split(',')[0]
				outfile_Ux_1st.write(res_Ux+'\n')
				i_Ux = 1
			elif i_Ux == 1:
				str_Ux=line.split(' ')[8]
				res_Ux=str_Ux.split(',')[0]
				outfile_Ux_2nd.write(res_Ux+'\n')
				i_Ux = 0
		elif line.startswith("smoothSolver:  Solving for Uy"):
			if i_Uy == 0:
				str_Uy = line.split(' ')[8]
				res_Uy = str_Uy.split(',')[0]
				outfile_Uy_1st.write(res_Uy + '\n')
				i_Uy = 1
			elif i_Uy == 1:
				str_Uy = line.split(' ')[8]
				res_Uy = str_Uy.split(',')[0]
				outfile_Uy_2nd.write(res_Uy + '\n')
				i_Uy = 0
		elif line.startswith("smoothSolver:  Solving for Uz"):
			if i_Uz == 0:
				str_Uz = line.split(' ')[8]
				res_Uz = str_Uy.split(',')[0]
				outfile_Uz_1st.write(res_Uz + '\n')
				i_Uz = 1
			elif i_Uz == 1:
				str_Uz = line.split(' ')[8]
				res_Uz = str_Uy.split(',')[0]
				outfile_Uz_2nd.write(res_Uz + '\n')
				i_Uz = 0
		elif line.startswith("GAMG:  Solving for p"):
			if i_p == 0:
				str_p=line.split(' ')[8]
				res_p=str_p.strip(',')
				outfile_p_1st.write(res_p+'\n')
				i_p = 1
			elif i_p == 1:
				str_p=line.split(' ')[8]
				res_p=str_p.strip(',')
				outfile_p_2nd.write(res_p+'\n')
				i_p = 0
		elif line.startswith("smoothSolver:  Solving for epsilon"):
			str_epsilon=line.split(' ')[8]
			res_epsilon=str_epsilon.split(',')[0]
			outfile_Epsilon.write(res_epsilon+'\n')
		elif line.startswith("smoothSolver:  Solving for k"):
			str_k=line.split(' ')[8]
			res_k=str_k.split(',')[0]
			outfile_k.write(res_k+'\n')
datafile.close()

outfile_Time.close()
outfile_CoMax.close()

outfile_Ux_1st.close()
outfile_Ux_2nd.close()
outfile_Uy_1st.close()
outfile_Uy_2nd.close()
outfile_Uz_1st.close()
outfile_Uz_2nd.close()

outfile_p_1st.close()
outfile_p_2nd.close()

outfile_Epsilon.close()
outfile_k.close()

Time=open("timeStep").readlines()
Ux=open("Ux_1st_residual").readlines()
Uy=open("Uy_1st_residual").readlines()
Uz=open("Uz_1st_residual").readlines()
p_1st=open("p_1st_residual").readlines()
p_2nd=open("p_2nd_residual").readlines()
k=open("k_residual").readlines()
epsilon=open("epsilon_residual").readlines()
MaxCo=open("MaxCo").readlines()

os.remove("timeStep")
os.remove("Ux_1st_residual")
os.remove("Uy_1st_residual")
os.remove("Uz_1st_residual")
os.remove("Ux_2nd_residual")
os.remove("Uy_2nd_residual")
os.remove("Uz_2nd_residual")
os.remove("p_1st_residual")
os.remove("p_2nd_residual")
os.remove("k_residual")
os.remove("epsilon_residual")
os.remove("MaxCo")

outfile_res = open("residuals",'w')
for i in range(0,len(Time)):
	outfile_res.write(str(Time[i]).replace("\n",' ')+ \
					str(Ux[i]).replace("\n",' ')+ \
					str(Uy[i]).replace("\n",' ')+ \
					str(Uz[i]).replace("\n",' ')+ \
					str(p_1st[i]).replace("\n",' ')+ \
					str(p_2nd[i]).replace("\n",' ')+ \
					str(epsilon[i]).replace("\n",' ')+ \
					str(k[i]).replace("\n",' ')+ \
					str(MaxCo[i]))
outfile_res.close()

import numpy as np
import matplotlib.pyplot as plt
plt.plot(Time,Ux,'r-',label="Ux")
plt.plot(Time,Uy,'r--',label="Uy")
plt.plot(Time,Uz,'r--',label="Uz")
plt.plot(Time,p_1st,'b-',label="p_1st")
plt.plot(Time,p_2nd,'b--',label="p_2nd")
plt.plot(Time,k,"g-",label="k")
plt.plot(Time,epsilon,"g--",label="epsilon")
plt.xlabel("time/s")
plt.ylabel("residuals")
plt.ylim(1e-5,1e-1)
plt.yscale('log')
plt.legend()
#plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.01)
plt.show()
