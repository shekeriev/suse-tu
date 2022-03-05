# Virtual Machines Instructions
This document describes the requirements and the steps to follow in order to prepare for the exercises. The information is organized in the following sections:
- Hardware and Software Requirements
- Virtual Machines Repository
- Hypervisor Instructions

## Hardware and Software Requirements
Your hardware is expected to meet the following requirements:
- An Intel or AMD-based CPU capable of virtualization
- At least 4 GB of RAM
- At least 10 GB of free hard disk space

In terms of software, you must have installed a recent version of **one** of the following virtualization solutions:
- Microsoft Hyper-V - free addition to Windows. More information on how to activate it can be found here: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
- Oracle VirtualBox - free solution that can be installed on both Windows and most Linux distributions. Can be downloaded from here: https://www.virtualbox.org/
- VMware Workstation - has free (WMware Workstation Player) and paid (WMware Workstation Pro) version. There is an option for a trial period of 30 days. Can be downloaded from here: https://www.vmware.com/products/workstation-pro.html

## Virtual Machines Repository
Virtual machine templates can be downloaded from here: https://zahariev.pro/go/suse-tu

Each template file's name follows this structure **xx-opensuse-leap-15.3[-gnome].yyy**. Where ***xx*** is the type of the virtualization solution and yyy is the type of the file - either *zip* or *ova*.

There are three sets of templates - one for every supported virtualization solution. They can be distinguished by the first two letters:
- **hv** stands for Microsoft Hyper-V
- **vb** stands for Oracle VirtualBox
- **vm** stands for VMware Workstation

Furthermore, for every solution, there are two different versions - one without a desktop environment (text-only mode) and one with a desktop environment (GNOME).

You may wonder how to choose and which one to pick. First, you must pick the set that matches your installed virtualization solution. Then, it is a matter of personal preference - with or without a graphical interface. For the purpose of the current initiative, each one will do the job. The text-based template is the preferred one because it is smaller and requires fewer resources.

Credentials for the virtual machines are:
- **root** with password set to **linux**
- **user** with password set to **linux**

## Hypervisor Instructions
Below you can find the instructions to import a template for your virtualization solution.

In the next sections, the following is assumed:
- the host operating system is Windows 10
- the virtual machines are stored in C:\VM
- we are working with the template without a graphical environment
- our new virtual machine will be named VM1

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
- change the connection to ***Default Switch*** (*) and click **Next**
- select the **Use an existing virtual hard disk** option 
- click the **Browse** button to select the extracted virtual hard disk and then click **Next**
- click **Finish**

(*) On the typical default installation of Hyper-V on Windows 10/11 there is a **Default Switch** installed. If you find it missing on your installation, follow the steps in the **Troubleshooting** section.

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
