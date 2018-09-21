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
Reading to "/dev/stdout" from 0x01ff7000..0x01ff8000 !
[                                                  ] 0%open-power-palmetto-v2.1-43-gc575972
        buildroot-2018.05.1-9-gc99f2eeb8c
        skiboot-v6.1
        hostboot-p8-d3025f5-p580ec27
        occ-p8-28f2cec
        linux-4.17.12-openpower1-p2b6da88
        petitboot-1.8.0
        machine-xml-e0fae90-p90e7e34
        hostboot-binaries-hw080118a.920
        capp-ucode-p9-dd2-v4
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
