# SUSE & Technical University Sofia
This document describes the requirements and the steps to follow in order to prepare for the exercises. The information is organized in the following sections:
- Hardware and Software Requirements
- Virtual Machines Repository
- Hypervisor Instructions

## Hardware and Software Requirements
Your hardware is expected to meet the following requirements:
- An Intel or AMD-based CPU capable of virtualization
- At least 4 GB of RAM
- At least 10 GB of free hard disk space

In terms of software, you must have installed one of the following virtualization solutions:
- Hyper-V - free addition to Windows. More information on how to activate it can be found here: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
- VirtualBox - a free solution that can be installed on both Windows and most Linux distributions. Can be downloaded from here: https://www.virtualbox.org/
- VMware Workstation - has free (WMware Workstation Player) and paid (WMware Workstation Pro) version. There is an option for a trial period of 30 days. Can be downloaded from here: https://www.vmware.com/products/workstation-pro.html

## Virtual Machines Repository
Virtual machine templates can be downloaded from here: https://zahariev.pro/go/suse-tu

Each template file's name follows this structure **xx-opensuse-leap-15.3[-gnome].yyy**. Where ***xx*** is the type of the virtualization solution and yyy is the type of the file - either *zip* or *ova*.

There are three sets of templates - one for every supported virtualization solution. They can be distinguished by the first two letters:
- **hv** stands for Hyper-V
- **vb** stands for Oracle VirtualBox
- **vm** stands for VMware Workstation

Furthermore, for every solution, there are two different versions - one without a desktop environment (text-only mode) and one with a desktop environment (GNOME).

You may wonder how to choose and which one to pick. First, you must pick the set that matches your installed virtualization solution. Then, it is a matter of personal preference - with or without a graphical interface. For the purpose of the current initiative, each one will do the job. The text-based template is the preferred one because it is smaller and requires fewer resources.

Credentials for the virtual machines are:
- **root** with password set to **linux**
- **user** with password set to **linux**

## Hypervisor Instructions
Bellow you can find the instructions to import a template for your virtualization solution.

### Hyper-V


### VirtualBox


### VMware Workstation