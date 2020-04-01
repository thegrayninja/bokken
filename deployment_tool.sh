#!/bin/bash
# Set "," as the field separator using $IFS
# and read line by line using while read combo



#example:
# deployment_tool.sh root@10.0.0.1 ue1-az-prod.pem

#Login=$1
#Key=$2


#echo "Login is $Login"
#echo "SSH Key is $Key"

input=$1
installerpackage="installer.deb"
declare -A installer
declare -A installstring1
declare -A installstring2
declare -A installstring3
declare -A username
ipconfig="ipconfig | findstr \"IPv4\""
cscid="kddd"

#echo ${arr[my key]}

installer["amazon"]="/aws-linux-2/falcon-sensor-5.28.0-9205.amzn2.x86_64.rpm"
installer["centos6"]="centos6/falcon-sensor-5.28.0-9205.el6.x86_64_CentOS6.rpm"
installer["centos7"]="centos7/falcon-sensor-5.28.0-9205.el7.x86_64_CentOS7.rpm"
installer["ubuntu"]="ubuntu/falcon-sensor_5.28.0-9205_amd64_ubuntu.deb"

installstring1["amazon"]="sudo yum install"
installstring1["centos6"]="sudo yum -y install ./falcon-sensor-5.28.0-9205.el6.x86_64_CentOS6.rpm"
installstring1["centos7"]="sudo yum install"
installstring1["ubuntu"]="sudo dpkg -i"

installstring2["amazon"]="sudo /opt/CrowdStrike/falconctl -s --cid=$cscid"
installstring2["centos6"]="sudo /opt/CrowdStrike/falconctl -s --cid=$cscid"
installstring2["centos7"]="sudo /opt/CrowdStrike/falconctl -s --cid=$cscid"
installstring2["ubuntu"]="sudo /opt/CrowdStrike/falconctl -s --cid=$cscid"

installstring3["amazon"]="sudo service falcon-sensor start"
installstring3["centos6"]="sudo service falcon-sensor start"
installstring3["centos7"]="sudo service falcon-sensor start"
installstring3["ubuntu"]="sudo systemctl start falcon-sensor"

username["amazon"]="ec2user"
username["centos6"]="centos"
username["centos7"]="centos"
username["ubuntu"]="ubuntu"

while IFS=',' read -r ipaddress keyname os
do
  os2=$(echo $os)
  getCentOSVersion="ssh ${username[$os2]}@$ipaddress -i $keyname cat /etc/centos-release"
  scpstring="scp -i $keyname ${installer[$os2]} ${username[$os2]}@$ipaddress: "
  sshstring1="ssh ${username[$os2]}@$ipaddress -i $keyname ${installstring1[$os2]}"
  sshstring2="ssh ${username[$os2]}@$ipaddress -i $keyname ${installstring2[$os2]}"
  sshstring3="ssh ${username[$os2]}@$ipaddress -i $keyname ${installstring3[$os2]}"

    #opsystem=$installstring1["$os"]
    #echo $installstring1[$os]

  echo $scpstring
  eval $getCentOSVersion

  eval $scpstring
  eval $sshstring1
  eval $sshstring2
  eval $sshstring3
  echo ""
  echo ""
done < $input

#eval $ipconfig

#ipconfig | findstr "IPv4"
