# prms-on-pegasus
A group effort on getting the Precipitation Runoff Modeling Simulation to run on Pegasus. We have attempted to execute a prms simulation as a simple process workflow on pegasus.

# PRMS - Precipitation Runoff Modeling Simulation
Important directory/files for any modeling simulation:
- `control/`
- `input/`
- `output/`
- `daxgen.py`
- `generate_dax.py`
- `plan_dax.py`
- `rc.txt`
- `tc.txt`
- `sites.xml`

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
