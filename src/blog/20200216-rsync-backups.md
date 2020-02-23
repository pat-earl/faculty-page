title: Making Automatic Backups on Linux
summary: Here we describe how to quickly setup efficient, automatic rolling backups on Linux. The backup at any particular week is simply a folder and can be accessed with your usual filemanager. Only the files that changed from the previous week occupy any space. The backups be made remotely, or locally.

{{summary}}

## Overview
Here's a quick overview of the process:

1. Suppose you already have backups of your data in the folders `backup/2020-02-14`, `backup/2020-02-15` from the last two days
2. To backup your data  today into `backup/2020-02-16` we *hard link* any file that hasn't changed from the previous backups, and then copy any file that has changed.
3. [rsync] now does this for you automatically, if you pass it the right options. A simple script that calls rsync correctly can be downloaded [here](https://gitlab.com/gi1242/perl-scripts/-/raw/master/backup.pl?inline=false)
4. A [systemd timer](https://www.freedesktop.org/software/systemd/man/systemd.timer.html) can be used to automate the process.

## Making the backup using rsync

To make the backup itself, you just need to run the command:

    rsync -xa -HAX --delete-after --fuzzy --fuzzy --delete-excluded \
        --exclude pat1 --exclude pat2 \
        --link-dest=../2020-02-14 --link-dest=../2020-02-15 \
        source-dir/ dest-dir/2020-02-16/

For a full eplanation of the options consult the [rsync] manual page.
The useful ones for our purpose are:

* `--exclude pat1`: Patterns of file / directory names you want excluded from the backup.
* `--link-dest=...`: All old backup directories need to be specified as paths relative to the destination backup directory.
* `dest-dir` is the destination directory, which can be a remote folder using a variety of supported protocols.

As time progresses you need to manually delete older backup directories.
All of this is a simple enough task that you can hack your own script quickly.
Or you can download my perl script [here](https://gitlab.com/gi1242/perl-scripts/-/raw/master/backup.pl?inline=false).
My script keeps:

* one backup a day for a week,
* one a week for 4 months,
* and one a month for two years.

If your target directory is on a remote host, then my script also requires you be able to `ssh` in there without having to type your password.

## Automating the process using a systemd timer

Once you have tuned your backup script to your liking, you can automate it easily using systemd as follows. (The older method to do this was using `cron`. Using `systemd` is simpler and more reliable.)

1. First setup a service that will notify you by email.
   Put the following in `~/.config/systemd/user/notify-email@.service`:

        :::ini
        [Unit]
        Description=Send email

        [Service]
        Type=oneshot
        ExecStart=sh -c 'systemctl --user status %i | \
            mailx -s "[SYSTEMD %i] Fail" gautam'

    (Replace `gautam` with your username of course.)

2. Now setup a service that will do the backups.
   Put the following in `~/.config/systemd/user/backup.service`:

        :::ini
        [Unit]
        OnFailure=notify-email@%i.service

        [Service]
        Type=oneshot
        ExecStart=/home/gautam/bin/backup \
            /home/gautam LOCAL_DST_DIR/backups -- -v
        ExecStart=/bin/bash -c '\
            eval "$(keychain --noask --agents ssh -Q --quiet --eval)"; \
            ~/bin/backup ~ REMOTEHOST:backups -- -v'

    Replace `/home/gautam` with the directory you want to backup.
    If you have a second hard drive, and want to do backups locally, then use the first `ExecStart` command.

    If you want to do backups remotely, then use the second `ExecStart` command.
    For this, you need a way to log in remotely without typing a password.
    The most common way of doing this is using `ssh` with a public/private key pair.
    If you have this setup, then your private key is typically encrypted and you only decrypt it in memory using `ssh-agent`.
    In order to let your backup run, you need to pass this information to systemd.
    I do it using [keychain](https://www.funtoo.org/Keychain) in the snippet above, but other was are possible too.

3. Finally setup a timer that runs the backup service.
   Put the following in `~/.config/systemd/user/backup.timer`:

        :::ini
        [Unit]
        Description="Automatically run backups"

        [Timer]
        OnCalendar=daily
        Persistent=true

        [Install]
        WantedBy=timers.target

4. Test it using

        systemctl --user start backup.service

    If there is a problem it should print an error message on the screen, and email you.
    You can also view the logs using

        journalctl --user-unit=backup.service

5. Once it is working, enable it so it runs automatically:

        systemctl --user enable backup.timer

[rsync]: https://rsync.samba.org
