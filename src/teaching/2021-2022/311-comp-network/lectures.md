title: CSC311 - Lectures

{% set lectures = (
    {"name": "Chapter 1 - Introduction", "file": "slides/chapter1.pdf"},
    {"name": "Networking Hardware", "file": "slides/hardware.pdf"},
    {"name": "Chapter 2 - Application Layer", "file": "slides/chapter2.pdf"},
    {"name": "DNS Overview", "file": "slides/dns.pdf"},
    {"name": "Telnet and FTP Overview", "file": "slides/telnet_and_ftp.pdf"},
    {"name": "Chapter 3 - Transport Layer", "file": "slides/chapter3.pdf"},
    {"name": "Load Balancing", "file": "slides/load_balancing.md"},
    {"name": "Chapter 4 - Network Layer", "file": "slides/chapter4.pdf"},
    {"name": "Chapter 5 - Control Plane Overview", "file": "slides/chapter5.pdf"}
) %}

## Course Lectures

Below are the PowerPoint slides from class in PDF form. You can also find the slides in their
original form on the Author's webpage: <https://gaia.cs.umass.edu/kurose_ross/ppt.php>

{% for lec in lectures -%}
* {{ lec['name'] }} - [Slide Form]({{ get_link(lec['file']) }})
{% endfor -%}

## Other Interesting Things

* [Cloudflare Blog - Facebook Outage](https://blog.cloudflare.com/october-2021-facebook-outage/)
* [Cloudflare's Learning Center](https://www.cloudflare.com/learning/)
    * Another resource for topic's covered in class & more. 

The TCP & UDP client/server programs I went over in class to demonstrate sockets are available 
on the Department's Linux machine. You can find them in this directory: `~earl/public/csc311`.
