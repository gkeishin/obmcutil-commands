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
$ ./rest_cmd -i xx.xx.xx.xx -c "cat /etc/os-release"
Executing: cat /etc/os-release
ID="openbmc-phosphor"
NAME="Phosphor OpenBMC (Phosphor OpenBMC Project Reference Distro)"
VERSION="v1.99.7-67"
VERSION_ID="v1.99.7-67-gdd05b96"
PRETTY_NAME="Phosphor OpenBMC (Phosphor OpenBMC Project Reference Distro) v1.99.7-67"
BUILD_ID="v1.99.7"
$
```

`PNOR VERSION`
```
$./rest_cmd -i xx.xx.xx.xx -c "/usr/sbin/pflash -r /dev/stdout -P VERSION"
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

$ 
```

`How to get system state`

`via command line`
```
$ ./rest_cmd -i xx.xx.xx.xx -c "/usr/sbin/obmcutil state"

Executing: /usr/sbin/obmcutil state
CurrentBMCState:    xyz.openbmc_project.State.BMC.BMCState.Ready
CurrentPowerState:  xyz.openbmc_project.State.Chassis.PowerState.On
CurrentHostState:   xyz.openbmc_project.State.Host.HostState.Running
```


`via REST`
```
$ ./rest_cmd -i xx.xx.xx.xx -o state
BMC state: Ready
Chassis Power state: On
Host state: Running
```
`



`Tool Usage help`

```
Usage:
rest_cmd -i <Host> -o <GET/PUT> -u <url path> -p <parmeters>
        -i | --host=   : Host IP
        -o | --option= : GET/PUT/POST REST request
        -u | --url=    : url path of the REST object
        -p | --parm=   : parameter
        -c | --command=   : command

         --------------------------------------------------------------
         *** Examples ***:
         *** Short cut commands for state/on/off/reboot ***:
         --------------------------------------------------------------
         Get BMC or PNOR info
         rest_cmd  -i xx.xx.xx.xx -c "cat /etc/os-release"
         rest_cmd  -i xx.xx.xx.xx -c "/usr/sbin/pflash -r /dev/stdout -P VERSION"
         --------------------------------------------------------------
         Get BMC FFDC
         rest_cmd  -i xx.xx.xx.xx -o ffdc
         --------------------------------------------------------------
         Get system state(BMC/Chassis/Host):
         rest_cmd  -i xx.xx.xx.xx -o state
         Poweron system:
         rest_cmd  -i xx.xx.xx.xx -o poweron
         Poweroff system:
         rest_cmd  -i xx.xx.xx.xx -o poweroff
         Reboot BMC:
         rest_cmd  -i xx.xx.xx.xx -o reboot
         --------------------------------------------------------------
         Get BMC state:
         rest_cmd  -i xx.xx.xx.xx -o bmc
         Get Host state:
         rest_cmd  -i xx.xx.xx.xx -o host
         Get Chassis power state:
         rest_cmd  -i xx.xx.xx.xx -o chassis
         --------------------------------------------------------------
         GET Operation:
         rest_cmd  -i xx.xx.xx.xx -o GET -u /xyz/openbmc_project/
         Enumerate Operation:
         rest_cmd  -i xx.xx.xx.xx -o GET -u /xyz/openbmc_project/enumerate
         --------------------------------------------------------------
         *** You can use it with url for other interfaces ****:
         --------------------------------------------------------------
         Host Power On:
         rest_cmd  -i xx.xx.xx.xx -o PUT -u /xyz/openbmc_project/state/host0/attr/RequestedHostTransition -p xyz.openbmc_project.State.Host.Transition.On
         ----------------------------------------------------------------

```
