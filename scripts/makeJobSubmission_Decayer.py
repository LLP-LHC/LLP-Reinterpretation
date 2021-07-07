#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
from collections import OrderedDict

outputDirectoryBase = "/storage/af/user/sixie/data/llp_gen/"
Base_DIR = "/storage/af/user/sixie/LLP-Reinterpretation/"
#Base_DIR = "/afs/cern.ch/work/s/sixie/public/Generator/LLP-Reinterpretation"

tarballfile = "/storage/af/user/sixie/LLP-Reinterpretation/tarball/Decayer_Delphes_tarball.tgz"
#DELPHESCARD_HIGGS = "delphes_card_CMS_CSCCluster_higgs_PileUp.tcl"
DELPHESCARD_HIGGS = "delphes_card_CMS_CSCCluster_higgs_PileUp_keepGenParticles.tcl"
DELPHESCARD_ALP = "delphes_card_CMS_CSCCluster_alp_PileUp.tcl"
DELPHESCARD_ALP = "delphes_card_CMS_CSCCluster_alp_PileUp.tcl"


datasetList = OrderedDict()
datasetList['ggH_HtoS1S2_S1andS2_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_0dot1.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_0dot26.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_0dot3.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_0dot5.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_1dot0.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_3dot0.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_3dot1.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_0dot1.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_0dot3.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_0dot6.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_0dot8.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_1dot0.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_1dot5.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_3dot25.txt",250, DELPHESCARD_HIGGS]]
datasetList['ggH_HtoS1S2_S1andS2_7GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_7dot0_AllToTauTau.txt",250, DELPHESCARD_HIGGS],
                                                 ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_7dot0.txt", 250, DELPHESCARD_HIGGS],
                                                 ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_7dot0.txt",250, DELPHESCARD_HIGGS]
]
datasetList['ggH_HtoS1S2_S1andS2_15GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_15dot0_AllToTauTau.txt", 40, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_15dot0_AllTobb.txt", 40, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_15dot0_AllTodd.txt", 40, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_15dot0.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_15dot0.txt",250, DELPHESCARD_HIGGS]
]

datasetList['ggH_HtoS1S2_S1andS2_25GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_25dot0.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_25dot0.txt",250, DELPHESCARD_HIGGS]]
datasetList['ggH_HtoS1S2_S1andS2_40GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_40dot0_AllToTauTau.txt", 40, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_40dot0.txt", 250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_40dot0.txt",250, DELPHESCARD_HIGGS]
]
datasetList['ggH_HtoS1S2_S1andS2_55GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_55dot0_AllToTauTau.txt",40, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_55dot0.txt",250, DELPHESCARD_HIGGS],
                                                  ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_55dot0.txt",250, DELPHESCARD_HIGGS]
]

datasetList['ggH_HtoS1S2_S1andS2_5GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_5dot0.txt", 250, DELPHESCARD_HIGGS],
                                                 ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_5dot0.txt",250, DELPHESCARD_HIGGS]
]

datasetList['ggH_HtoS1S2_S1andS2_3dto5GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Scalar/phi/phi_3dot5.txt", 250, DELPHESCARD_HIGGS],
                                                 ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/Vectors/dark_photon/dark_photon_3dot5.txt",250, DELPHESCARD_HIGGS]
]

datasetList['ggalp_1GeV_3Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot32.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot52.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot57.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot52.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot67.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot72.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot77.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot82.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot87.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot92.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot97.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot02.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot07.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot22.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot32.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot47.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_1dot62.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_2dot02.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_2dot47.txt",22, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_3dot0.txt",22, DELPHESCARD_ALP]]
datasetList['ggalp_5GeV_3Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_4dot0.txt",43, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_5dot0.txt",43, DELPHESCARD_ALP]]
datasetList['ggalp_7GeV_3Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_6dot0.txt",42, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_7dot0.txt",42, DELPHESCARD_ALP],
                                   ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_8dot0.txt",42, DELPHESCARD_ALP]]
datasetList['ggalp_10GeV_3Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_9dot0.txt",42, DELPHESCARD_ALP],
                                    ["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_10dot0.txt",42, DELPHESCARD_ALP]]
datasetList['walp_1W0B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",43, DELPHESCARD_ALP]]
datasetList['zalp_1W0B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",42, DELPHESCARD_ALP]]
datasetList['zalp_0W1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",41, DELPHESCARD_ALP]]
datasetList['zalp_1W1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",42, DELPHESCARD_ALP]]
datasetList['zalp_1Wm1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",42, DELPHESCARD_ALP]]
datasetList['gammaalp_1W0B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",41, DELPHESCARD_ALP]]
datasetList['gammaalp_0W1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",17, DELPHESCARD_ALP]]
datasetList['gammaalp_1W1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",41, DELPHESCARD_ALP]]
datasetList['gammaalp_1Wm1B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",41, DELPHESCARD_ALP]]
datasetList['gammaalp_1Wtm2B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",41, DELPHESCARD_ALP]]
datasetList['zalp_1Wtm2B_1GeV_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/ALPs/ALPGG_0dot07.txt",42, DELPHESCARD_ALP]]

datasetList['iDM_1GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_1mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_3GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_3mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_6GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_6mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_10GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_10mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_20GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_20mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_23GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_23mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_30GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_30mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_33GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_33mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_40GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_40mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_60GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_60mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_100GeV_Dp1_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot1_100mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_1GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_1mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_3GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_3mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_6GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_6mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_10GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_10mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_20GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_20mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_23GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_23mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_30GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_30mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_33GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_33mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_40GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_40mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_60GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_60mass.txt",42, DELPHESCARD_ALP]]
datasetList['iDM_100GeV_Dp05_2Jets'] = [["/storage/af/user/sixie/LLP-Reinterpretation/branchingRatios/inel/inel_0dot05_100mass.txt",42, DELPHESCARD_ALP]]





for datasetName in datasetList.keys():
    
    for elem in datasetList[datasetName]:
        decayTableName = elem[0].split('/')[-1].split('.')[0]

        print "Preparing workflow for dataset :" + datasetName + " and decay " + decayTableName + "\n"
    
        subDirName = datasetName + "_" + decayTableName
        outputDirectory = outputDirectoryBase + "/" + subDirName + "/"  
        decayTableFile = elem[0]
        numberOfJobs = elem[1] 
        delphesCard = elem[2]

        #####################################
        #create run script and executable
        #####################################
        #print ("cat " + Base_DIR + "/condor/" + subDirName + "/run_template.sh" + " | sed 's/XX_MODELNAME_XX/" + datasetName + "/g' " + " | sed 's/XX_DECAYTABLE_XX/" + decayTableFile + "/'" + " | sed 's/XX_OUTPUTDIR_XX/" + outputDirectory + "\//'" +  " > " + Base_DIR + "/condor/" + subDirName + "/run_job.sh")
        os.system("mkdir -p " + Base_DIR + "/condor/" + subDirName + "/log/" )
        os.system("mkdir -p " + Base_DIR + "/condor/" + subDirName + "/out/" )
        os.system("mkdir -p " + Base_DIR + "/condor/" + subDirName + "/err/" )
        os.system("cp " + Base_DIR + "/scripts/run_decayer_job_caltech_tier2.sh " +  Base_DIR + "/condor/" + subDirName + "/run_template.sh")
        os.system("cat " + Base_DIR + "/condor/" + subDirName + "/run_template.sh" + " | sed 's/XX_MODELNAME_XX/" + datasetName + "/g' " + " | sed 's/XX_DECAYTABLE_XX/" + decayTableFile.replace("/","\/") + "/'" + " | sed 's/XX_OUTPUTDIR_XX/" + outputDirectory.replace("/","\/") + "\//'" + " | sed 's/XX_DELPHESCARD_XX/" + delphesCard + "/'" +  " > " + Base_DIR + "/condor/" + subDirName + "/run_job.sh")
    
        #####################################
        #Create Condor JDL file
        #####################################
        tmpCondorJDLFile = open(Base_DIR + "/condor/" + subDirName + "/task.jdl","w+")
        tmpCondorJDLFileTemplate = """
Universe  = vanilla
Executable = ./run_job.sh
"""
        tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
        tmpCondorJDLFile.write("Arguments = $(I)" + "\n")

        tmpCondorJDLFileTemplate = """
Log = log/job.$(Cluster).$(Process).log
Output = out/job.$(Cluster).$(Process).out
Error = err/job.$(Cluster).$(Process).err
x509userproxy = $ENV(X509_USER_PROXY)
"""
        tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
        tmpCondorJDLFile.write("Transfer_Input_Files = " + tarballfile + ", " + Base_DIR + "/condor/" + subDirName + "/run_job.sh " + "\n")

        tmpCondorJDLFileTemplate = """
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Requirements=(TARGET.OpSysAndVer=="CentOS7" && regexp("blade.*", TARGET.Machine))
RequestMemory = 2000
RequestCpus = 1
RequestDisk = 4
+RunAsOwner = True
+InteractiveUser = true
+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"
+SingularityBindCVMFS = True


"""
        tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)

        tmpCondorJDLFileTemplate = """

# Jobs selection
Queue I from (
"""

        tmpCondorJDLFile.write(tmpCondorJDLFileTemplate)
        for i in range(0,numberOfJobs):
            tmpCondorJDLFile.write(str(i)+"\n")
        tmpCondorJDLFile.write(")\n")
        tmpCondorJDLFile.close()

