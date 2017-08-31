#!/bin/bash
# A quick simple bash script

if [[ -z "$1" || -z "$2" ]]; then
   echo "---------------------------------------------"
   echo " Please enter BMC IP/hostname and option"
   echo "---------------------------------------------"
   echo "To delete eSEL/Error log entries"
   echo "clear_bmc_elog.sh  <BMC_IP>  <logging>"
   echo ""
   echo "To delete BMC dump entries"
   echo "clear_bmc_elog.sh  <BMC_IP>  <dump>"
   echo "---------------------------------------------"
   exit 0
fi

BMC_IP=$1
DBUS_PATH=$2

echo "----------------------------------------------"
echo "Creating REST session to BMC: $BMC_IP"
echo "----------------------------------------------"
curl -c cjar -b cjar -k -H "Content-Type: application/json" -X POST https://$BMC_IP/login -d "{\"data\": [ \"root\", \"0penBmc\" ] }"

echo ""
echo "----------------------------------------------"
echo "Session established to $BMC_IP"
echo "----------------------------------------------"

list_entry=`curl -c cjar -b cjar -k -H 'Content-Type: application/json' -X GET  https://$BMC_IP/xyz/openbmc_project/$DBUS_PATH/list | grep -v callout | grep -v manager`

entries=`echo "$list_entry" | grep entry`

if [[ -z "$entries" ]]; then
    echo "----------------------------------------------"
    echo "No Error/BMC Dump entry(s) found"
    echo "----------------------------------------------"
    exit 0
fi

echo "----------------------------------------------"
for i in $entries; do
   entry=`echo $i | sed "s/,/ /g"`
   entry=`echo $entry | sed "s/\"//g"`
   echo ""
   echo "Deleting https://$BMC_IP/$entry"
   curl -c cjar -b cjar -k -H "Content-Type: application/json" -X DELETE  https://$BMC_IP/$entry
done

echo ""
echo "----------------------------------------------"
echo "All error log/BMC dump deleted"
echo "----------------------------------------------"
