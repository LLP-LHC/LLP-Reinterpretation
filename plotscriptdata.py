# Written by Giovanna Cottin (gfcottin@gmail.com)
import os,sys
import numpy as np
import math

mX    = np.linspace(250, 3000, 20)
lam   = np.linspace(0.01, 0.01, 1)

#Vlnu2 = np.array([1e-01])
### for login node
#madgraph_path = '/storage/user/christiw/login-1/christiw/LLP/MG5_aMC_v2_8_1'
#card_dir = '/storage/user/christiw/login-1/christiw/LLP/HNL/scripts'
### for Christina's macbook pro
madgraph_path = '/storage/af/user/jmina/LLP-Reinterpretation/MG5_aMC_v2_7_3'
#card_dir = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig2/Plot1_Cards'
output_dir = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig5/Plot3_Data_0803'
#if not os.path.isdir(output_dir+"/m"+str(mass)+"_l"+str(lamv)):os.makedirs(output_dir+"/m"+str(mass)+"_l"+str(lamv))
if not os.path.isdir(output_dir):os.makedirs(output_dir)
#if not os.path.isdir(output_dir+''):os.makedirs(output_dir+'HNL_mg5_GRID_tau')

#Mixing in electron sector
for mass in mX:
    for lamv in lam:
        #sqmix2 = np.sqrt(float(mix2))
	#if mass >= 1: mass = int(mass)
        f = open(output_dir+"/m"+str(round(mass, 2))+"_l"+str(lamv),'w')
        f.write("import model /storage/af/user/jmina/LLP-Reinterpretation/madgraph_models/SFV_2HDM_uptype\n")
        #f.write("define w= w+ w-\n")
        #f.write("define e= e+ e-\n")
        #f.write("generate p p > w, (w > e n1)\n") #on shell
        #f.write("generate p p > w+ > e n1\n") #off shell
        #f.write("add process p p > w- > e n1\n")
        f.write("define p = g u c d s u~ c~ d~ s~\n")
	f.write("define j = g u c d s u~ c~ d~ s~\n")
        f.write("define l+ = e+ mu+\n")
        f.write("define l- = e- mu-\n")
        f.write("define vl = ve vm vt\n")
        f.write("define vl~ = ve~ vm~ vt~\n")
	f.write("generate g g > h1 h1 [QCD]\n")
	#f.write("add process p p > w j, (w > e n1)\n")
#	f.write("add process p p > w+ j j, (w+ > e n1)\n")
#	f.write("add process p p > w- j j, (w- > e n1)\n")
#	f.write("add process p p > w+ j j j, (w+ > e n1)\n")
#	f.write("add process p p > w- j j j, (w- > e n1)\n")
#	f.write("add process p p > w+ j j j j, (w+ > e n1)\n")
#	f.write("add process p p > w- j j j j, (w- > e n1)\n")
	f.write("output "+output_dir+"/Plot3_Data_G/m"+str(round(mass, 2))+"_l"+str(lamv)+"\n")
        f.write("launch\n")
        f.write("set nevents 1000\n")
        f.write("set use_syst False\n")
        f.write("set l2 0.0\n")
        f.write("set l3 0.0\n")
        f.write("set lR7 0.0\n")
        f.write("set cosbma 0.025\n")
        f.write("set xi 0.0\n")
        f.write("set mh1 125.0\n")
        f.write("set mh2 "+str(mass)+"\n")
        f.write("set mh3 "+str(mass)+"\n")
        f.write("set mhc "+str(mass)+"\n")
        f.write("set GDR1x1 "+str(lamv)+"\n")
        f.write("set GDR2x2 0.0\n")
        f.write("set GDR3x3 0.0\n")
        f.write("set Wh2 Auto\n")
        f.write("set Wh3 Auto\n")
        f.write("set Whc Auto\n")
#        f.write("generate_events\n")
#        f.write(card_dir+"/param_card_HNL.dat\n")
#        f.write(card_dir+"/run_card_HNL.dat\n")
        ##f.write("set time_of_flight 1e-25\n") ## get displaced neutrinos/set in run_card
#        f.write("set numixing 1 "+str(sqmix2)+"\n")
#        f.write("set numixing 5 0\n")
#        f.write("set numixing 9 0\n")
#        f.write("set MASS 9900012 "+str(mass)+"\n")
#        f.write("set MASS 9900014 1.000000e+03\n") #decouple other N
#        f.write("set MASS 9900016 1.000000e+03\n")
#        f.write("set DECAY 9900012 Auto\n")
        f.close()
#Mixing in muon sector
#for mass in mN:
  #  for mix2 in Vlnu2:
 #       sqmix2 = np.sqrt(mix2)
#        f = open(output_dir+"HNL_mg5_GRID_mu/HNL_mg5_GRID_mu-"+str(mass)+"-"+str(mix2),'w')
        #f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
       # f.write("define w= w+ w-\n")
      #  f.write("define mu= mu+ mu-\n")
     #   f.write("generate p p > w, (w > mu n2)\n")
    #    f.write("output "+output_dir+"HNL_GRID_mu/HNL_GRID_mu-"+str(mass)+"-"+str(mix2)+"\n")
   #     f.write("launch -i "+output_dir+"HNL_GRID_mu/HNL_GRID_mu-"+str(mass)+"-"+str(mix2)+"\n")
  #      f.write("generate_events\n")
 #       f.write(card_dir+"/param_card_HNL.dat\n")
#        f.write(card_dir+"/run_card_HNL.dat\n")
       # f.write("set numixing 1 0\n")
      #  f.write("set numixing 5 "+str(sqmix2)+"\n")
     #   f.write("set numixing 9 0\n")
    #    f.write("set MASS 9900012 1.000000e+03\n")
   #     f.write("set MASS 9900014 "+str(mass)+"\n") 
  #      f.write("set MASS 9900016 1.000000e+03\n")
 #       f.write("set DECAY 9900014 Auto\n")
#        f.close()
#Mixing in tau sector
#for mass in mN:
  #  for mix2 in Vlnu2:
 #       sqmix2 = np.sqrt(mix2)
#        if mass >= 1: mass = int(mass)
        #f = open(output_dir+"HNL_mg5_GRID_tau/HNL_mg5_GRID_tau-"+str(mass)+"-"+str(mix2),'w')
       # f.write("import model SM_HeavyN_Gen3Mass_NLO\n")
      #  f.write("define w= w+ w-\n")
     #   f.write("define tau= ta+ ta-\n")
    #    f.write("define j = g u c d s u~ c~ d~ s~\n")
   #     f.write("generate p p > w, (w > tau n3)\n")
  #      f.write("add process p p > w j, (w > tau n3)\n")
 #       f.write("output "+output_dir+"HNL_GRID_tau/HNL_GRID_tau-"+str(mass)+"-"+str(mix2)+"\n")
#        f.write("launch -i "+output_dir+"HNL_GRID_tau/HNL_GRID_tau-"+str(mass)+"-"+str(mix2)+"\n")
        #f.write("generate_events\n")
       # f.write(card_dir+"/param_card_HNL.dat\n")
      #  f.write(card_dir+"/run_card_HNL.dat\n")
     #   f.write("set numixing 1 0\n")
   #     f.write("set numixing 5 0\n")
    #    f.write("set numixing 9 "+str(sqmix2)+"\n")
  #      f.write("set MASS 9900012 1.000000e+03\n")
 #       f.write("set MASS 9900014 1.000000e+03\n") 
#        f.write("set MASS 9900016 "+str(mass)+"\n")
#        f.write("set DECAY 9900016 Auto\n")
#        f.close()

