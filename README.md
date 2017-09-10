# lftpd
A lame FTP daemon-ish server, created with [pyftpdlib](https://github.com/giampaolo/pyftpdlib) and setproctitle. Used only on Unix and Unix-like system such as Linux, FreeBSD, Solaris, macOS and others.

## Installation
This not meant to be used production as this program has not benchmarked; you have been warned.

Install these packages from pip:<br>
`pip3 install pyftpdlib`<br>
`pip3 install setproctitle`<br>

If you don't have `pip` installed, install it via your package manager for painless installation.

## Running
Running is very simple:
`python3 ftpserver.py`

No flags and no extensions! I will add extensions once this FTP server becomes more mature and more stable.

## Troubleshooting
As far as I know, you didn't install something correctly. Make sure you installed everything. If nothing works, email me.

## Contributions
They are always welcome! Email me or send in a PR.
