title: Blocking SSH brute force attackes on Docker containers with sshguard
summary: [sshguard](https://sshguard.net/) protects hosts from brute force attacks by monitoring logs and blocking attackers. It works (almost) out of the box to protect hosts. However, if you are running a Docker container that also provides ssh access (e.g. like [gitolite](https://gitolite.com/gitolite/index.html)) then brute force attacks aren't blocked by default. Here's how to block brute force attacks on your container.

{{summary}}

1. First make sure your docker container is generating ssh logs. Check your `Dockerfile` is passing `-e` to sshd:

        :::docker
        CMD ["-D", "-e"]
        ENTRYPOINT ["/usr/sbin/sshd"]

    and make sure you see the logs when you run `docker logs gitolite`.
    (Here `gitolite` is the name of my docker container. Replace it with whatever you call your container.)

2. Assuming you're running `systemd`, then pass your container logs to `journald`.
   (You don't have to do this, but it's a bit more reliable this way with container restarts.)
   Edit `/etc/docker/daemon.json` (or create it if it doesn't exist):

        :::json
        {
            "log-driver": "journald"
        }

    Restart docker (you might also have to restart / rebulid your containers).
    Then check you can see your container logs by `journalctl -o cat CONTAINER_NAME=gitolite`

3. Now install `sshguard` on the host, and pass your container logs to sshguard on the host.
   Edit `/etc/sshguard/sshguard.conf` and set `LOGREADER` as follows:

        :::shell
        LOGREADER="LANG=C journalctl -afb -p info -o cat -n1 \
            SYSLOG_IDENTIFIER=sshd SYSLOG_IDENTIFIER=sendmail \
            SYSLOG_IDENTIFIER=postfix/smtpd + CONTAINER_NAME=gitolite"

4. Docker passes incoming traffic to the container before sshguard sees it.
   So, by default,  `sshguard` **wont block** any traffic to your containers by default.
   To fix this, copy `/usr/lib/x86_64-linux-gnu/sshg-fw-nft-sets` to `/etc/sshguard/sshg-fw-nft-sets-local`.
   Now change it so that sshguard hooks `prerouting` instead of `input`, and change the priority from `-10` to `-200`.
   (On my system docker's firewall rules have priority `-100`. You need sshguard to run before, so any number smaller than `-100` will do.)
   Here are the changes I made:

        :::diff
        --- /usr/lib/x86_64-linux-gnu/sshg-fw-nft-sets	2019-02-11 22:11:23.000000000 -0500
        +++ /etc/sshguard/sshg-fw-nft-sets-local	2019-10-31 22:10:03.475621324 -0400
        @@ -24,8 +24,8 @@
             run_nft "add table" "" 4
             run_nft "add table" "" 6
         
        -    run_nft "add chain" "${NFT_CHAIN}"' { type filter hook input priority -10 ; }' 4
        -    run_nft "add chain" "${NFT_CHAIN}"' { type filter hook input priority -10 ; }' 6
        +    run_nft "add chain" "${NFT_CHAIN}"' { type filter hook prerouting priority -200 ; }' 4
        +    run_nft "add chain" "${NFT_CHAIN}"' { type filter hook prerouting priority -200 ; }' 6
         
             # Create sets
             run_nft "add set" "${NFT_SET} { type ipv4_addr; flags interval; }" 4

    Make these changes take effect by setting `BACKEND` in `/etc/sshguard/sshguard.conf`:

        :::shell
        BACKEND="/etc/sshguard/sshg-fw-nft-sets-local"

5. Restart `sshguard`, and you should be all set.
   Be sure to attack your host and container from some outside machine and ensure your traffic is actually getting blocked.
