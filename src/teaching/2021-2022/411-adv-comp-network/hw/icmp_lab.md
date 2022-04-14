title: ICMP Lab
breadcrumb: ../index.md

**Due:**
: Friday, April 22, 2022 End-of-Day

## Description

You'll be focusing on the ICMP protocol for this lab. Launch your mininet VM to complete this assignment. 

Before starting the steps below, here is some recommended reading on the protocol:

- [Chapter 5 Slides (Slide #31)](https://faculty.kutztown.edu/earl/teaching/2021-2022/311-comp-network/slides/chapter5.pdf)
- [Cloudflare ICMP](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)

Prepare a document so you can record your answers. The questions you need to answer
will be placed with the steps below.

Complete the following steps.

1. Before launching mininet, run the following command to install `traceroute`
   * `sudo apt install traceroute`
   * If you get any errors at this point, try running `apt update` and then the command again.
   * Any further issues contact me.
2. Make sure you are in the home directory (Should be there when you login) and type the following command:
   * `sudo -E ./mininet/mininet/examples/nat.py`
   * This will create a mininet environment with access to the internet.
3. Once in the mininet CLI, test your connect to the internet with this command:
   * `h1 ping 8.8.8.8`
   * You should see something like *64 bytes from 8.8.8.8*. You can hit CTRL+C to stop the ping command.
   * If you don't see that, you have a networking issue with your VM. Again contact me in that case. 
4. Launch a terminal for host 1 (`xterm h1`) and do the following in the terminal window that appears:
   1. Run this command: `wireshark 2>/dev/null &`
      * A Wireshark window should pop up. 
   2. Start capturing on *h1-eth0* 
   3. Run the following command: `ping -c5 1.1.1.1`
   4. Stop packet capture in wireshark when the command completes by pressing the red stop button.
   5. Answer the following:
      1. Look at the first ICMP request. What is the value of the type field? 
      2. What are the source and destination IP addresses?
      3. What internet protocol is being used to transport this packet?
      4. Look at the first ICMP reply. What is the value of the type field?
      5. What are the source and destination IP addresses of this response?
   6. Back in your Wireshark window, restart packet capture by clicking the blue shark fin. 
   7. Now run this command: `ping -c5 -t5 1.1.1.1`
   8. Stop the packet capture again.
   9. Answer the following questions:
      1. The ping command should have a different output now. Inspect the first ICMP request and specificity the information in the IPv4 details.  What is the TTL value?
      2. Now look at the first response. What is the ICMP type? 
      3. What are the source and destination IP addresses of this response?
      4. Why isn't the source IP address the IP address target of the ping command?

## Submission

Submit your answers to me in .docx or .pdf format via an email attachment. 