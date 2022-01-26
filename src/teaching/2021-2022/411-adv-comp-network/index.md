infotable: 0
title: CSC411 - Advanced Networking Individualized Instruction
stylesheet: ../../course.css
{% from 'includes/macros.j2' import course_info_table with context -%}
{% from get_file('course_info.j2') import course %}

{{course_info_table(course)}}

## Links

* [CS&IT Academic Integrity Policy](https://www.kutztown.edu/Departments-Offices/A-F/ComputerScienceInformationTechnology/Documents/Student%20Resources/AcademicIntegrityPolicy.pdf)
* [**Resources**]({{get_link('resources.md')}})

## Course Description
This course deals with the theory, implementation, and administration of networks. It is also 
concerned with the various layers of the Internet architecture stack, with concentration on layers
3 and 4. The primary protocols of these layers, Transmission Control Protocol (TCP) and Internet
Protocol (IP), will be studied in detail. Network addressing and related protocols will be covered. 

## Assignments

* Week 1 - [Get Mininet Running]({{get_link('./hw/mininet_setup.md')}})

## Topics

*Under Construction*

<table id="schedule">
    <colgroup>
        <col span="1" style="width: 65%;">
        <col span="1" style="width: 35%;">
    <thead>
        <tr>
            <th scope="col" style="text-align: center;">Topic(s)</th>
            <th scope="col" style="text-align: center;">Reading(s)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Local Area Networks & Topologies
            </td>
            <td>
                <ul>
                    <li>
                        <a href="https://faculty.kutztown.edu/earl/teaching/2021-2022/311-comp-network/slides/chapter6.pdf">
                            Link Layer Slides
                        </a>
                    </li>
                    <li>
                        <a href="https://faculty.kutztown.edu/earl/teaching/2021-2022/311-comp-network/slides/hardware.pdf">
                            Networking Hardware
                        </a>
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>
                IPv4 - Addressing, Subnets, Etc.
            </td>
            <td>
                TBD
            </td>
        </tr>
        <tr>
            <td>
                IPv6
            </td>
            <td>
                TBD
            </td>
        </tr>
        <tr>
            <td>
                DHCP - Dynamic Host Configuration Protocol
            </td>
            <td>
                TBD
            </td>
        </tr>
        <tr>
            <td>
                IP Forwarding (Routing)
            </td>
            <td>
                TBD
            </td>
        </tr>
        <tr>
            <td>
                Packet Processing 
            </td>
            <td>
                TBD
            </td>
        </tr>
        <tr>
            <td>
                Network Management
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                Network Security
            </td>
            <td>
            </td>
        </tr>
    </tbody>
</table>