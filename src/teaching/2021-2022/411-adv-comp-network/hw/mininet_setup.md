title: Mininet Setup
breadcrumb: ../index.md

**Due:**
: End of Week 2 - Flexible

## Steps:

We're going to try and use [*Mininet*](http://mininet.org) as supplement for this course. It provides
a quick and easyish way to create virtual networks on your machine. 

You'll be using their Virtual Machine to avoid having to do *too* much setup.

**Downloads**:

* You'll need a way to run VM's, one of the two are recommended:
    * [VirtualBox](https://www.virtualbox.org/)
    * [VMWare Workstation 16 Player](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html)
        * *You don't need to pay for a license, select `for non-commercial use` when installing*
* Mininet:
    * <https://github.com/mininet/mininet/releases/>
    * Download the OVF zip file for `ubuntu-20.04.1-legacy-server-amd64`

1. Once mininet is downloaded, unzip the contents to a directory that's easy to find. 
2. Follow the steps outlined in [Mininet's VM Setup Notes](http://mininet.org/vm-setup-notes/)
3. Once the VM is setup, complete *Part 1* of the [Mininet Walkthrough](http://mininet.org/vm-setup-notes/)

To do X11 forwarding (GUI) through SSH, you'll need a X11 viewer. For windows it's recommended to use
[VcXSrv](https://sourceforge.net/projects/vcxsrv/). You'll need to enable *X11 Forwarding* in PuTTY. 
The setting is found under *Connection -> SSH -> X11*. 

The setup for Mac is different, Google something like *"X11 ssh forwarding on MacOS"*
This article may help, but I haven't personally vetted it: <https://www.cyberciti.biz/faq/apple-osx-mountain-lion-mavericks-install-xquartz-server/>

If you run into any issues, email me or stop by office hours.