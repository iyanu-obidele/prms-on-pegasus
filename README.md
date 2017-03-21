# prms-on-pegasus
A group effort on getting the Precipitation Runoff Modeling Simulation to run on Pegasus. We have attempted to execute a prms simulation as a simple process workflow on pegasus.

# PRMS - Precipitation Runoff Modeling Simulation
Important directory/files for any modeling simulation:
- `control/`		- contains the control files for the said simulation
- `input/`		- contains all input files for the said simulation
- `output/`		- contains all output files for the said simulation
- `daxgen.py`		- python DAX generator
- `generate_dax.py`	- shell script that adds Pegasus python library to path and generates DAX using `daxgen.py`
- `plan_dax.py`		- plans the workflow and submits it to the right specified job pool, condorpool.
- `rc.txt`		- replication control file. Contains the fully qualified paths for files used in the context of the workflow.
- `tc.txt`		- transformation control file. Contains the paths to executables, along with architecture requirements of executables used in the context of the workflow.
- `sites.xml`		- specifies, the directories to be used for scratch, or directories to write output to. etc.
- `pegasus.properties`	- Tells Pegasus where to find rc.txt, tc.txt and other important config files.

# How to Run
- Step 1:
  Generate dax (Direct-Acylic Graph XML) for workflow using command: `./generate_dax.sh <name_of_daxFile> <name_of_controlFile> [name_of_outputFile]`.

- Step 2:
  Edit `tc.txt` to reflect the new fully qualified path for the prms executable.

- Step 3:
  Edit `rc.txt` to reflect the fully qualified path of input control file

- Step 4:
  Edit `sites.xml` to reflect correct fully qualified scratch and output space

- Step 5:
  Run `./plan_dax <name_of_daxFile>` to submit workflow to HTCondor

# How to view Pegasus Dashboard
You would need to create a tunnel to achieve this, since we only have remote access to the server running pegasus. Recall that Pegasus is running on `dewey.cs.pdx.edu`

- Step 1:
  create a tunnel like so `ssh -L <sourcePort>:127.0.0.1:<destinationPort> <user>@dewey.cs.pdx.edu`

- Step 2:
  Start up a pegasus service using `pegasus-service`. This starts the service on port 5000. So destination port above should be set to 5000. 
  To start service on a custom port run `pegasus-service -p <port-no>`. Remember to use the destinationPort as specified in step-1 above.

- Step 3:
  View dashboard on your machine at `https://localhost:<sourcePort>` 

# TL:DR
For a single workflow run, enter the `sagehen-on-pegasus` directory and simply execute `./plan_dax prms.dax`

For multiple simulations in a workflow (concurrent/parallel runs), enter the `sample-with-multiple-simulations` directory and run `./plan_dax.sh prms2.dax`

Remember to always change the paths in the input files to their fully qualified paths.
