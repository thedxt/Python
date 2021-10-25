# Some Company Bit Defender Silent install
 
# the BitDefender Gravity Zone ID to match the install to the correct customer
$GZID = "GZ_PACKAGE_ID=TheGZID_HERE"

# url to get BitDefender installer
$BDURL = "BitDefender MSI Download URL here"

# check if temp exists if not make it
$temp = "temp"

if (-not (Test-Path $Env:SystemDrive\$temp))
{
New-Item -ItemType Directory $Env:SystemDrive\$temp | out-null
}

# enable TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# download the file to temp
Invoke-WebRequest -Uri $BDURL -OutFile "$Env:SystemDrive\$temp\BEST_downloaderWrapper.msi"


# install BitDefender silently with no reboot and like with the gavity zone id
msiexec /i "$Env:SystemDrive\$temp\BEST_downloaderWrapper.msi" /qn $GZID

write-host "BitDefender install is running"