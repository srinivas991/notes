### WINDOWS

`Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber`

```
get-wmiobject ref: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1
https://ss64.com/ps/get-wmiobject.html
https://adamtheautomator.com/get-wmiobject/
```

Some other useful classes that can be used with Get-WmiObject are Win32_Process to get a process listing, Win32_Service to get a listing of services Win32_Bios to get BIOS information. We can use the ComputerName parameter to get information about remote computers. GetWmiObject can be used to start and stop services on local and remote computers.

Program Files -	On 32-bit systems, all 16-bit and 32-bit programs are installed here. On 64-bit systems, only 64-bit programs are installed here.

AppData -	Per user application data and settings are stored in a hidden user subfolder (i.e., cliff.moore\AppData). Each of these folders contains three subfolders. The Roaming folder contains machine-independent data that should follow the user's profile, such as custom dictionaries. The Local folder is specific to the computer itself and is never synchronized across the network. LocalLow is similar to the Local folder, but it has a lower data integrity level. Therefore it can be used, for example, by a web browser set to protected or safe mode.

System, System32, SysWOW64	- Contains all DLLs required for the core features of Windows and the Windows API. The operating system searches these folders any time a program asks to load a DLL without specifying an absolute path.

to view tree structure of any windows directory

`tree "c:\Program Files (x86)\VMware"`
`tree c:\ /f | more`


We can list out the NTFS permissions on a specific directory by running either icacls from within the working directory or icacls C:\Windows against a directory not currently in.

`icacls c:\windows`

#### SHARES

The Server Message Block protocol (SMB) is used in Windows to connect shared resources like files and printers. It is used in large, medium, and small enterprise environments

Share permissions
Permission	Description
Full Control -	Users are permitted to perform all actions given by Change and Read permissions as well as change permissions for NTFS files and subfolders
Change -	Users are permitted to read, edit, delete and add files and subfolders
Read -	Users are allowed to view file & subfolder contents


when a Windows system is part of a workgroup, all netlogon requests are authenticated against that particular Windows system's SAM database. When a Windows system is joined to a Windows Domain environment, all netlogon requests are authenticated against Active Directory.

The primary difference between a workgroup and a Windows Domain in terms of authentication, is with a workgroup the local SAM database is used and in a Windows Domain a centralized network-based database (Active Directory) is used. We must know this information when attempting to logon & authenticate with a Windows system

Firewall rules on desktop systems can be centrally managed when joined to a Windows Domain environment through the use of Group Policy. Group Policy concepts and configurations are outside of the scope of this module.

Anytime we see a gray checkmark next to a permission, it was inherited from a parent directory. By default, all NTFS permissions are inherited from the parent directory. In the Windows world, the C:\ drive is the parent directory to rule all directories unless a system administrator were to disable inheritance inside a newly created folder’s advanced Security settings.

The `net share` command allows us to view all the shared folders on the system

Event Viewer is another good place to investigate actions completed on Windows

#### Services and Processes

`Get-Service | ? {$_.Status -eq "Running"} | select -First 2 |fl`

Windows has three categories of services: Local Services, Network Services, and System Services. Services can usually only be created, modified, and deleted by users with administrative privileges. Misconfigurations around service permissions are a common privilege escalation vector on Windows systems.

https://docs.microsoft.com/en-us/windows/win32/rstmgr/critical-system-services

lsass.exe - local security authority subsystem service

When a user attempts to log on to the system, this process verifies their log on attempt and creates access tokens based on the user's permission levels. LSASS is also responsible for user account password changes. All events associated with this process (logon/logoff attempts, etc.) are logged within the Windows Security Log

sysinternals => internet-accessible file share by typing `\\live.sysinternals.com\tools`

serives.msc / sc (cmdline)

```
sc qc service_name
sc stop service_name
sc config service_name binpath=c:\...
sc sdshow service_name
```

every windows object has a security descriptor, which we can see for a service using sc sdshow wuauserv

security descriptor has 2 parts, DACL(discretionary) and SACL(system), represented by D: an S: in the security descriptor

Generally, a DACL is used for controlling access to an object, and a SACL is used to account for and log access attempts.

eg: `D:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)`

this is just DACL part ^^

This amalgamation of characters crunched together and delimited by opened and closed parentheses is in a format known as the Security Descriptor Definition Language (SDDL)

`Get-ACL -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List`

`wmic os list brief` => get sys info
`Get-WmiObject -Class Win32_OperatingSystem | select SystemDirectory,BuildNumber,SerialNumber,Version | ft`

Each of the security principals on the system has a unique security identifier (SID). The system automatically generates SIDs. A SID consists of the Identifier Authority and the Relative ID (RID). In an Active Directory (AD) domain environment, the SID also includes the domain SID.

