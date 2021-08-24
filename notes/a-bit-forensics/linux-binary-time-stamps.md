# linux binary time stamps

when a server is compromised by an attacker, its possible that the attacker has uploaded a backdoor into your system.

this is a bit interesting, not the usual `crontab` reverse shell, or a reverse shell in a `bashrc` file that gets executed when ever a user logs into the server.

here, there are some binaries on our box, lets say `ping`, which is usually executed by people when they log into a box, or `ls` for that matter, so what an attacker does is, he clones the `GNU-utils` or whatever the repository might be and he adds the script for backdoor, it can be just a single shell command, and compile the `binary` from the source code, and replace your `ls` binary that you installed along with your OS with the custom binary that he compiled with the `backdoor`, and every time you run `ls`, it works normally because nothing changed, and it is compiled from the source code. So every time you run, it might be giving a `reverse-shell` to the attacker.

here is what can help with that kind of investigation,

when you have the binaries that come along with the machine installation, or any package managers for that matter, when you look at the timestamps of those binaries, lets just go to `/usr/bin` and check this.

```text
ls -la /usr/bin --time-style=full
```

![](../../.gitbook/assets/image%20%2823%29.png)

so, the trick here is, most package managers don't record the microseconds on those timestamps when they get installed, and when a user interactively puts something in the path or anywhere really, the microsecond timestamp also gets recorded.

Lets copy the bash binary from `/usr/bin/bash` to `/tmp/bash` and see this

![](../../.gitbook/assets/image%20%2826%29.png)

we can see the full timestamp here, unlike the `.0000...` we've seen before. This can help with any investigation if you suspect anything similar

this is sourced from [https://youtu.be/JfonPpbX-oI?t=1589](https://youtu.be/JfonPpbX-oI?t=1589)

