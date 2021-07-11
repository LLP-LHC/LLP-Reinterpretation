#!/bin/bash


if [ "$1" = "" ]; then
    echo "no task_name provided"
    echo "usage: source sumit_condor.sh <task_name> <model_file>"
    echo "QUIT!!"
    exit 1
fi

if [ "$2" = "" ]; then
    echo "no model_file provided"
    echo "usage: source sumit_condor.sh <task_name> <model_file>"
    echo "QUIT!!"
    exit 1
fi

##################################
###define input list and task_name
##################################
model_file=$2
task_name=$1
model_dir=madgraph_generation
top_directory=`git rev-parse --show-toplevel`
eos_dir=/storage/cms/store/user/cpena/llp_gen
executable=MG5_aMC_v2_9_3/bin/mg5_aMC
tarball=/storage/af/user/cpena/work/new_clean_for_llp/CMSSW_9_4_20/src/LLP-Reinterpretation_v3.tar.gz
CMSSW_DIR=/storage/af/user/cpena/work/new_clean_for_llp/CMSSW_9_4_20/
echo "top directory: "$top_directory

###################################################
#create output dir in eos and send the files there
##################################################
#output_dir="/eos/uscms/"${eos_dir}/${task_name}
#echo ${output_dir}
#mkdir -p ${output_dir}
eval `scram unsetenv -sh`
echo gfal-mkdir -p gsiftp://transfer-lb.ultralight.org/${eos_dir}/${task_name}
gfal-mkdir -p gsiftp://transfer-lb.ultralight.org/${eos_dir}/${task_name}

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd ${top_directory}
eval `scram runtime -sh`
#make clean;make -j 16
#make -j 16
cd -

#################################
#obtain number of total files
#################################
#nfiles=`cat ${input_list} | wc -l`

#############################################################
#compute number of jobs according to number of files_per_job
#############################################################
#njobs=$((nfiles/files_per_job))
#missing_file=$((nfiles%files_per_job))

#echo $njobs
#if (( $missing_file > 0 ));then
#njobs=$((njobs+1))
#fi

#echo $njobs

##################################################
####create task directory inside condor directory
#################################################
condor_dir=${top_directory}/"condor"
scripts_dir=${top_directory}/"scripts"
task_name_dir=${top_directory}/"condor"/${task_name}
mkdir -p ${task_name_dir}
#####################################
#get run_job.sh file from scripts dir
#####################################
job_n=1
cp ${scripts_dir}/run_job_caltech_tier2.sh ${task_name_dir}/run_job.sh

printf "\n" >> ${task_name_dir}/run_job.sh
printf "cd "${CMSSW_DIR} >> ${task_name_dir}/run_job.sh
printf '\neval `scram runtime -sh`' >> ${task_name_dir}/run_job.sh
printf "\ncd -" >> ${task_name_dir}/run_job.sh
printf "\n###########################" >> ${task_name_dir}/run_job.sh
printf "\n#run executable" >> ${task_name_dir}/run_job.sh
printf "\n###########################" >> ${task_name_dir}/run_job.sh
printf '\ntar -zxf LLP-Reinterpretation_v3.tar.gz' >> ${task_name_dir}/run_job.sh
#printf '\ncp '${model_file}' LLP-Reinterpretation/.' >> ${task_name_dir}/run_job.sh
#printf '\ncd LLP-Reinterpretation' >> ${task_name_dir}/run_job.sh
#printf '\nsource setup.sh' >> ${task_name_dir}/run_job.sh
printf '\npython2  '${executable}' $1' >> ${task_name_dir}/run_job.sh
printf '\nls -ltrh' >> ${task_name_dir}/run_job.sh
#printf '\nls -ltrh htoS1S2/htoS1S2_2j_pythia/Events/run_01/' >> ${task_name_dir}/run_job.sh
printf '\neval `scram unsetenv -sh`' >> ${task_name_dir}/run_job.sh
printf "\n\ngfal-copy -rf llp_gen/madgraph_pythia/Events/run_01 gsiftp://transfer-lb.ultralight.org//"${eos_dir}/${task_name}/${task_name}"_mad5_pythia8_run_"${job_n} >> ${task_name_dir}/run_job.sh
#printf "\ncd ../; rm -rf LLP-Reinterpretation" >> ${task_name_dir}/run_job.sh

##################################################
####create condor log directories inside task name
#################################################
mkdir -p ${task_name_dir}/"log"
mkdir -p ${task_name_dir}/"out"
mkdir -p ${task_name_dir}/"err"

condor_submit_file=${task_name_dir}/"condor_submit.condor"
current_input_list=${task_name_dir}/$i

printf "Universe = vanilla\n" > ${condor_submit_file}
printf "Executable = "${task_name_dir}"/run_job.sh\n" >> ${condor_submit_file}

#printf "Transfer_Input_Files = "${top_directory}/${executable}", "${top_directory}/${model_dir}/${model_file} >> ${condor_submit_file}
printf "Transfer_Input_Files = "${top_directory}/${model_dir}/${model_file}", "${tarball} >> ${condor_submit_file}
#printf "Transfer_Input_Files = "${tarball} >> ${condor_submit_file}
printf "\nnotify_user = $(whoami)@cern.ch\n" >> ${condor_submit_file}

printf "Should_Transfer_Files = YES \n" >> ${condor_submit_file}
printf "WhenToTransferOutput = ON_EXIT\n" >> ${condor_submit_file}
printf 'Requirements=(TARGET.OpSysAndVer=="CentOS7" && regexp("blade.*", TARGET.Machine))\n' >> ${condor_submit_file}
printf "RequestMemory = 2000\n" >> ${condor_submit_file}
printf "RequestCpus = 1\n" >> ${condor_submit_file}
printf "RequestDisk = 4\n" >> ${condor_submit_file}
printf "+RunAsOwner = True\n" >> ${condor_submit_file}
printf "+InteractiveUser = true\n" >> ${condor_submit_file}
#printf '+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/bbockelm/cms:rhel7"\n' >> ${condor_submit_file}
printf '+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel7-m202006"\n' >> ${condor_submit_file}
printf "+SingularityBindCVMFS = True\n" >> ${condor_submit_file}
printf "run_as_owner = True\n" >> ${condor_submit_file}
printf "x509userproxy = \$ENV(X509_USER_PROXY)\n" >> ${condor_submit_file}
printf "\n" >> ${condor_submit_file}
printf "Output = "${task_name_dir}"/out/llp_gen.\$(Cluster)_\$(Process).stdout\n" >> ${condor_submit_file}
printf "Error  = "${task_name_dir}"/err/llp_gen.\$(Cluster)_\$(Process).stderr\n" >> ${condor_submit_file}
printf "Log    = "${task_name_dir}"/log/llp_gen.\$(Cluster)_\$(Process).log\n" >> ${condor_submit_file}

printf "\n" >> ${condor_submit_file}
printf "Arguments = ${model_file} \n" >> ${condor_submit_file}
printf "Queue\n" >> ${condor_submit_file}


condor_submit $condor_submit_file
