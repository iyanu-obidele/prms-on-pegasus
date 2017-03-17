#!/bin/bash
set -e
pegasus_lite_version_major="4"
pegasus_lite_version_minor="7"
pegasus_lite_version_patch="4"
pegasus_lite_enforce_strict_wp_check="true"
pegasus_lite_version_allow_wp_auto_download="true"

. pegasus-lite-common.sh

pegasus_lite_init

# cleanup in case of failures
trap pegasus_lite_signal_int INT
trap pegasus_lite_signal_term TERM
trap pegasus_lite_exit EXIT

echo -e "\n################################ Setting up workdir ################################"  1>&2
# work dir
export pegasus_lite_work_dir=$PWD
pegasus_lite_setup_work_dir

echo -e "\n###################### figuring out the worker package to use ######################"  1>&2
# figure out the worker package to use
pegasus_lite_worker_package

echo -e "\n############################# executing the user tasks #############################"  1>&2
# execute the tasks
set +e
pegasus-kickstart -n prms -N ID0000001 -o listing.txt -R condorpool  -L process -T 2017-03-14T20:59:08-07:00 prms control/sagehen.control
job_ec=$?
set -e

