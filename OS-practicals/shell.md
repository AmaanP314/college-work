## a. Display OS version, release number, kernel version

```bash
#!/bin/bash
# os_info.sh

# Distribution description (e.g. "Ubuntu 24.04 LTS")
echo -n "OS: "
lsb_release -ds          # requires lsb-release package citeturn0search0

# Release number only (e.g. "24.04")
echo -n "Release: "
lsb_release -rs          # requires lsb-release package citeturn0search0

# Kernel version (e.g. "5.15.0-56-generic")
echo -n "Kernel: "
uname -r                 # uname: print kernel release citeturn0search1
```

---

## b. Display top 10 processes in descending CPU usage

```bash
#!/bin/bash
# top_procs.sh

# List PID, command, and %CPU, sort by CPU descending, show top 10
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 11   # includes header citeturn1search0
```

---

## c. Display processes with highest memory usage

```bash
#!/bin/bash
# high_mem.sh

# List PID, command, and %MEM, sort by memory descending, show top 10
ps -eo pid,comm,%mem --sort=-%mem | head -n 11   # includes header citeturn1search11
```

---

## d. Display current logged‑in user and login name

```bash
#!/bin/bash
# user_info.sh

# Effective username (same as `id -un`)
echo -n "Current user: "
whoami          # prints effective user name citeturn2search0

# Original login name
echo -n "Login name: "
logname         # prints the name you used to log in citeturn2search1
```

---

## e. Display current shell, home directory, OS type, PATH, and current working directory

```bash
#!/bin/bash
# env_info.sh

# User’s login shell
echo -n "Shell: "
echo "$SHELL"                         # $SHELL environment variable citeturn3search12

# Home directory
echo -n "Home: "
echo "$HOME"                          # $HOME environment variable citeturn3search12

# OS type (e.g. "GNU/Linux")
echo -n "OS type: "
uname -o                             # uname: print operating system name citeturn0search1

# PATH setting
echo -n "PATH: "
echo "$PATH"                         # $PATH environment variable citeturn3search12

# Current working directory
echo -n "PWD: "
pwd                                  # print working directory citeturn3search12
```

---

**Notes:**

- On some distributions, `lsb_release` may require installation (e.g. `sudo apt install lsb-release`).
- All of these commands are POSIX‐compliant and should work in most Linux environments.
- You can combine several of these into a single script if preferred.

---

Absolutely! Here's a **single shell script** containing all five parts (a to e), neatly organized and ready to run. You can copy and save it as something like `system_info.sh`, then run with:

```bash
bash system_info.sh
```

---

### 🖥️ `system_info.sh`

```bash
#!/bin/bash

echo "=============================="
echo "a. OS Version, Release, Kernel"
echo "=============================="
echo "OS Version: $(uname -o)"
echo "Release Number: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2 | tr -d '\"')"
echo "Kernel Version: $(uname -r)"
echo

echo "============================================"
echo "b. Top 10 Processes (Descending by CPU Usage)"
echo "============================================"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 11
echo

echo "====================================="
echo "c. Process with Highest Memory Usage"
echo "====================================="
ps -eo pid,comm,%mem --sort=-%mem | head -n 6
echo

echo "==============================="
echo "d. Logged In User and Log Name"
echo "==============================="
echo "Logged in user: $(whoami)"
echo "Login name: $LOGNAME"
echo

echo "=============================================================="
echo "e. Shell, Home Directory, OS Type, PATH, Working Directory"
echo "=============================================================="
echo "Current Shell: $SHELL"
echo "Home Directory: $HOME"
echo "Operating System Type: $(uname)"
echo "Current PATH Setting: $PATH"
echo "Current Working Directory: $(pwd)"
```

---

### ✅ What It Does

- **(a)** Shows OS type/version/release using `uname` and `/etc/os-release`
- **(b)** Lists top 10 processes by CPU usage with `ps`
- **(c)** Lists top processes by memory usage
- **(d)** Shows current user and login name
- **(e)** Displays shell, home, OS type, path, and working directory

---

Let me know if you want to save output to a file, add color, or make it interactive!
