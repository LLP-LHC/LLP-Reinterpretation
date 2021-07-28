#!/bin/bash

jobNumber=$1
modelName="XX_MODELNAME_XX"
decayTable="XX_DECAYTABLE_XX"
outputDir="XX_OUTPUTDIR_XX"
delphesCard="XX_DELPHESCARD_XX"

echo "JobNumber : ${jobNumber}"
echo "modelName : ${modelName}"
echo "Decay Table file: ${decayTable}"

mkdir -p ${outputDir}


#######################
#debugging purposes
#######################
voms-proxy-info --all
ls -l

############################
#define exec and setup cmssw
############################
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

###########################
#get cmssw environment
###########################
which scramv1
scramv1 project CMSSW CMSSW_9_4_20
cd CMSSW_9_4_20
eval `scram runtime -sh`
cd -

#untar stuff...
tar xzf Decayer_Delphes_tarball.tgz

###########################
#run Decayer
###########################
pythia8Dir=${PWD}/LLP-Reinterpretation/MG5_aMC_v2_9_3/HEPTools/pythia8/
export PATH=${pythia8Dir}/bin:${PATH}
export PYTHIA8DATA=${pythia8Dir}/share/Pythia8/xmldoc
echo $PYTHIA8DATA
export LD_LIBRARY_PATH=${PWD}/LLP-Reinterpretation/MG5_aMC_v2_9_3/HEPTools/boost/lib:${LD_LIBRARY_PATH}


#cd /storage/af/user/sixie/LLP-Reinterpretation/Pythia8Decayer_install/

Pythia8Decayer_install/bin/Pythia8Decayer -c Pythia8Decayer_install/share/Pythia8Decayer/default.dat -i /storage/af/user/cpena/data/llp_gen/${modelName}/tag_1_pythia8_events_split_${jobNumber}.hepmc -o ./DecayerOutput_split_${jobNumber}.hepmc -d ${decayTable}

#cp -v ./DecayerOutput_split_${jobNumber}.hepmc ${outputDir}/

###########################
#run delphes
###########################
cd Delphes
echo "Use Delphes Card: ${delphesCard}"
./DelphesHepMC cards/${delphesCard} ../DelphesOutput_split_${jobNumber}.root ../DecayerOutput_split_${jobNumber}.hepmc
cd -

###########################
#save to output
###########################
rm -v DecayerOutput_split_${jobNumber}.hepmc
mv -v DelphesOutput_split_${jobNumber}.root ${outputDir}/
ls -ltr ${outputDir}/

echo "Job completed"
