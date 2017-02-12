username: https://www.google.com/accounts/o8/id?id=AItOawl2ORpZHrIrOfELP3ETcGoSJah2eMfa7Ow
name: Sachin
avatar: http://cdn.libravatar.org/avatar/83d8636057d5904cb2ddc4591efd201d1c9acb2bf3fba4ea658d5f5c75dc1fcf
subject: SSH Tunnel
date: 2014-09-09 19:22:01

As an alternative to the SOCKS proxy, you could set up an [SSH tunnel](http://matt.might.net/articles/ssh-hacks/): 

`ssh you@campus.machine.edu -L <port>:paywalledjournal.com:<port>`

(With <port> for HTTP access usually being 80.)
