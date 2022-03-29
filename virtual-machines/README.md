# Virtual Machines Instructions

This document describes the requirements and the steps to follow in order to prepare for the exercises. The information is organized in the following sections:

- [Hardware Requirements](#hardware-requirements)
- [Hardware Requirements (Apple M1)](#hardware-requirements-apple-m1)
- [Software Requirements](#software-requirements)
- [Software Requirements (Apple M1)](#software-requirements-apple-m1)
- [Virtual Machines Repository](#virtual-machines-repository)
- [Hypervisor Instructions](#hypervisor-instructions)
- [Troubleshooting](#troubleshooting)

The most up to date version of this document can be found here: <https://github.com/shekeriev/suse-tu/tree/main/virtual-machines>

## Hardware Requirements

*Please note that this applies to all AMD and Intel based computers including the Apple products that use Intel chips.*

Your hardware is expected to meet the following requirements:

- 64-bit Intel or AMD-based CPU capable of virtualization
- at least 4 GB of RAM
- at least 10 GB of free hard disk space

You can check if your CPU supports virtualization using the following resources:

- for Intel CPUs - <https://ark.intel.com/content/www/us/en/ark.html>
- for AMD CPUs - <https://www.amd.com/en/products/specifications/processors>
- any CPU - <https://www.cpu-world.com/>

Even if your processor supports virtualization, the operating system still may not see and be able to use it. To check how the OS sees the capabilities of the CPU, you may use the following:

- for Windows - use the CPU-Z utility (<https://www.cpuid.com/softwares/cpu-z.html>) or the Coreinfo utility (<https://docs.microsoft.com/en-us/sysinternals/downloads/coreinfo>)
- for Linux distributions, execute the following command (if the result is greater than 0, you are good to go):

        grep -E 'vmx|svm' /proc/cpuinfo | wc -l

- for macOS on Intel CPU, execute the following command (look for VMX):

        sysctl -a | grep machdep.cpu.features

Do not forget to activate virtualization support in the BIOS if you haven't done so.

## Hardware Requirements (Apple M1)

Nothing special here. All Apple computers based on the M1 chip support virtualization.

## Software Requirements

In terms of software, you must be working on a recent version of Windows 10/11, macOS, or Linux distribution. In addition, you must have installed a recent version of **one** of the following virtualization solutions (hypervisors):

- **Microsoft Hyper-V** - a free addition to Windows (1). More information on how to activate it can be found here: <https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v>
- **Oracle VirtualBox** - a free solution that can be installed on both Windows and most Linux distributions. Can be downloaded from here: <https://www.virtualbox.org/>
- **VMware Workstation** - has free (***WMware Workstation Player***) and paid (***WMware Workstation Pro***) version. There is an option for a trial period of 30 days. Can be downloaded from here: <https://www.vmware.com/products/workstation-pro.html>

*(1) Hyper-V role is available and supported only on Windows Pro, Enterprise, and Education editions.*

If you are working on a Linux distribution and want to experiment, you can install **KVM**. There is a template for it as well.

In general, if you are wondering which one to select, go for Oracle VirtualBox. It is simple, free, and offers broad support for both host and guest operating systems.

## Software Requirements (Apple M1)

There are just a few virtualization options currently for **Apple M1** based machines. One such solution is the **UTM** (<https://mac.getutm.app/>) application. You must download it and install it. The process is trivial and won't be covered here.

## Virtual Machines Repository

Virtual machine templates can be downloaded from here: <https://zahariev.pro/go/suse-tu>

Each template file's name follows this structure ***xx-opensuse-leap-15.3[-gnome].yyy***. Where ***xx*** is the type of the virtualization solution and ***yyy*** is the type of the file - either ***zip*** or ***ova***.

There are three (1) sets of templates - one for every supported virtualization solution. They can be distinguished by the first two letters:

- **hv** stands for **Microsoft Hyper-V**
- **vb** stands for **Oracle VirtualBox**
- **vm** stands for **VMware Workstation**

*(1) There is one additional template ***kv-opensuse-leap-15.3.qcow2***. It is a text-only installation of openSUSE Leap 15.3. It is to be used with the KVM hypervisor.*

Furthermore, for every solution, there are two different versions - one without a desktop environment (text-only mode) and one with a desktop environment (GNOME).

You may wonder how to choose and which one to pick. First, you must pick the set that matches your installed virtualization solution. Then, it is a matter of personal preference - with or without a graphical interface. For the purpose of the current initiative, each one will do the job. The text-based template is the preferred one because it is smaller and requires fewer resources.

Credentials for the virtual machines are:

- **root** with password set to **linux**
- **user** with password set to **linux**

## Hypervisor Instructions

Below you can find the instructions to import a template for your virtualization solution.

In the next sections, the following is assumed:

- the host operating system is **Windows 10**
- the virtual machines are stored in **C:\VM**
- we are working with the template without a graphical environment
- our new virtual machine will be named **VM1**

If your setup is different, then you must adjust accordingly.

### Microsoft Hyper-V

To create one virtual machine from the template, we must follow these steps:

- download the template **hv-opensuse-leap-15.3.zip** locally
- extract its contents to the folder where the virtual machines are stored
- rename the resulting file **hv-opensuse-leap-15.3.vhdx** to ***VM1.vhdx***
- open the **Hyper-V Manager**
- go to the main menu and select **Action** > **New** > **Virtual machine**
- on the first screen click **Next**
- enter ***VM1*** in the **Name** field and click **Next**
- select **Generation 1** and click **Next**
- if you want, change the value of the **Startup memory** to something bigger, for example to ***2048***. It will work with the default value as well
- remove the tick from the **Use Dynamic Memory for this virtual machine** option and click **Next**
- change the connection to ***Default Switch*** (1) and click **Next**
- select the **Use an existing virtual hard disk** option
- click the **Browse** button to select the extracted virtual hard disk and then click **Next**
- click **Finish**

*(1) On the typical default installation of Hyper-V on Windows 10/11 there is a **Default Switch** installed. If you find it missing on your installation, follow the steps in the **Troubleshooting** section.*

Before you start the machine, there is one more step to execute - to turn off the **automatic checkpoints**. Follow these steps:

- select the virtual machine (while turned off)
- go to the main menu and select **Action** > **Settings**
- scroll down to **Management** and select **Checkpoints**
- deselect the option **Use automatic checkpoints**
- select the option **Production checkpoints**
- confirm the changes by clicking on the **OK** button

Now, we are ready to power on our new virtual machine and start experimenting with it. The typical interactions with the virtual machine include:

- power it on - select the machine in the list and from the main menu select **Action** > **Start**
- connect to it - select the machine in the list and from the main menu select **Action** > **Connect**
- power if off - select the machine in the list and from the main menu select **Action** > **Shut Down**

The above commands plus many more are available in the context menu (select the machine and right-click on it) of the machine as well.

### Oracle VirtualBox

To create one virtual machine from the template, we must follow these steps:

- download the template **vb-opensuse-leap-15.3.ova** locally
- start the **Oracle VM VirtualBox** application
- go to the main menu and select **File** > **Import Appliance**
- click the button next to the **File:** field
- navigate to the folder where you downloaded the template
- select it and click the **Open** button
- click **Next**
- change the name of the machine to ***VM1*** in the **Name** field and click **Import**
- after a while the process will finish and the machine will appear in the list of available virtual machines

Now, we are ready to power on our new virtual machine and start experimenting with it. All commands that we will need are in the **Machine** section of the main menu. They are available in the context menu (select the machine and right-click on it) of the machine as well.

### VMware Workstation

To create one virtual machine from the template, we must follow these steps:

- download the template **vm-opensuse-leap-15.3.ova** locally
- start the **VMware Workstation** application
- go to the main menu and select **File** > **Open**
- navigate to the folder where you downloaded the template
- select it and click the **Open** button
- enter ***VM1*** in the **Name for the new virtual machine** field and click **Import**
- after a while the process will finish and the machine will appear in the library of the application

Now, we are ready to power on our new virtual machine and start experimenting with it. All commands that we will need are in the **VM** section of the main menu. They are available in the context menu (select the machine and right-click on it) of the machine as well.

### KVM *

This is an alternative hypervisor that those of you who are working on a Linux distribution can use. Keep in mind that it may be challenging in the beginning especially compared to Oracle VirtualBox.

To create one virtual machine from the template, we must follow these steps:

- download the template **kv-opensuse-leap-15.3.qcow2** locally and copy it to the folder where the virtual disks are stored (usually, it is **/var/lib/libvirt/images/**)
- open the **Virtual Machine Manager** application and connect to your KVM
- go to the main menu and select **File** > **New Virtual Machine**
- select **Import existing disk image** and click **Forward**
- click the **Browse** button, select the template and confirm with **Choose Volume**
- if the field **Choose the operating system you are installing** does not get populated, type ***opensuse*** and select the closest match (for example, ***openSUSE Leap 15.1***) and click **Forward**
- set the values for memory and CPU (1024 or 2048 for memory and 1 for CPU are more than enough) and click **Forward**
- adjust the name of the machine and click **Finish**
- after a while the process will finish and the machine will appear in the library of the application

The VM will be started automatically. All commands that we will need are shown as buttons on the toolbar. They are available in the context menu (select the machine and right-click on it) of the machine as well.

### UTM *

This one is applicable only to **Apple M1** based machines.

To create one virtual machine from the template, we must follow these steps:

- download the template **utm-opensuse-tumbleweed.zip** locally and extract it to a folder of your choice
- if you want to adjust the name of the machine, you must rename the extracted file
- open the **UTM** application
- go to the main menu and select **File** > **Open**
- select the extracted template and confirm with **Open**
- this will register the virtual machine
- next, you can click on the settings button (top right corner) and adjust any of the options you want. Once done, confirm with **Save**

The VM should be started manually. All commands that we will need are shown as buttons on the toolbar. They are available in the context menu (select the machine and right-click on it) of the machine as well.

## Troubleshooting

**Hyper-V Default Switch missing**

In general, it is difficult to recreate the default switch. Instead, we can create a basic NAT switch which will get us covered. The only drawback is that it won't have any DHCP functionalities. So, we should manually configure the network settings of our virtual machines. Thus, in addition to the switch, we can create a small virtual machine that will act as DHCP server.

Should you want to create just the switch and take care of the rest by yourself (for example, manual setup of IP addresses on the virtual machines), check this link <https://zahariev.pro/files/hyper-v-nat-switch.html> and follow the instructions there.

Of course, we can go with the complete solution - switch + DHCP virtual machine. We can do it either manually, or use an automated solution.

If you are looking for an automated solution, you check this procedure:

- open a PowerShell session with **Run as administrator** option (right click on the icon and select the option)
- navigate to the root folder
        
        cd c:\

- change temporary the execution policy (you must confirm when asked)
    
        Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

- download the setup script

        Invoke-WebRequest -UseBasicParsing -Uri https://zahariev.pro/files/setup-hv-dhcp.ps1 -OutFile setup-hv-dhcp.ps1

- source the script (this will make all the functions there available)

        . .\setup-hv-dhcp.ps1

- now, to create the switch and the special VM that will act as a DHCP server

        Create-HVDHCPSetup

- should you want to delete the artifacts, execute this instead

        Remove-HVDHCPSetup

As a result of the above, we will end up with a new switch (NAT vSwitch) and a tiny virtual machine (HVDHCP) that will act as DHCP server to the virtual machines that are connected to the switch. The default network settings are:

- network - 192.168.99.0/24
- default gateway - 192.168.99.1
- DHCP server - 192.168.99.2
- address range - 192.168.99.100 - 192.168.99.199

The credentials for the tiny virtual machine are **root** / **Parolka1!**.

Don't forget to link the virtual machines (either existing or new) to the newly created switch (NAT vSwitch).
