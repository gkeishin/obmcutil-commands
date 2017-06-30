# obmcutil-commands
Open BMC REST and Command execution client code


`Prerequisite`

Install the following packages

sudo apt-get install python-pip python-dev build-essential 

sudo pip install --upgrade pip 

pip install paramiko
pip install requests


How to use the tool: `rest_cmd`

`BMC VERSION`
```
rango@ubuntu:~/obmcutil-commands$ ./rest_cmd -i xx.xx.xx.xx -c "cat /etc/os-release"
Executing: cat /etc/os-release
ID="openbmc-phosphor"
NAME="Phosphor OpenBMC (Phosphor OpenBMC Project Reference Distro)"
VERSION="v1.99.7-67"
VERSION_ID="v1.99.7-67-gdd05b96"
PRETTY_NAME="Phosphor OpenBMC (Phosphor OpenBMC Project Reference Distro) v1.99.7-67"
BUILD_ID="v1.99.7"
rango@ubuntu:~/obmcutil-commands$
```

`PNOR VERSION`
```
rango@ubuntu:~/obmcutil-commands$ ./rest_cmd -i xx.xx.xx.xx -c "/usr/sbin/pflash -r /dev/stdout -P VERSION"
Executing: /usr/sbin/pflash -r /dev/stdout -P VERSION
Reading to "/dev/stdout" from 0x02820000..0x02821000 !
[                                                  ] 0%IBM-witherspoon-ibm-OP9_v1.17_1.47

	op-build-v1.17-105-gf736aad-dirty
	buildroot-2017.02.2-7-g23118ce
	skiboot-5.6.0-158-ga1e0a047b2a0
	hostboot-f2250d8
	linux-4.11.6-openpower1-pe9f6e0b
	petitboot-v1.4.3-pa7356d8
	machine-xml-5b59a1d
	occ-1dc97a6
	hostboot-binaries-711147e
	capp-ucode-9c73e9f
	sbe-02021c6

[==================================================] 100%

rango@ubuntu:~/obmcutil-commands$ 
```


`How to get system state`

`via REST`
```
rango@ubuntu:~/obmcutil-commands$ ./rest_cmd -i xx.xx.xx.xx -o state
BMC state: Ready
Chassis Power state: On
Host state: Running
```

`via BMC util command`
```
rango@ubuntu:~/obmcutil-commands$ ./rest_cmd -i xx.xx.xx.xx -c "/usr/sbin/obmcutil state"

Executing: /usr/sbin/obmcutil state
CurrentBMCState:    xyz.openbmc_project.State.BMC.BMCState.Ready
CurrentPowerState:  xyz.openbmc_project.State.Chassis.PowerState.On
CurrentHostState:   xyz.openbmc_project.State.Host.HostState.Running
rango@ubuntu:~/obmcutil-commands$ 
```
