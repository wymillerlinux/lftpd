# lftpd
A lame FTP daemon-ish server, created with [pyftpdlib](https://github.com/giampaolo/pyftpdlib) and setproctitle. Used only on Unix and Unix-like system such as Linux, FreeBSD, Solaris, macOS and others. Now Dockerized! Run the Dockerfile to have this run in a container! Note that the Docker image is running on Debian Linux.

## Installation

First, I assume you have Python 3, git, and optionally Docker, to run this software. If you don't have these pieces of software, please use your package manager to install them.

### Vanilla Python 3
This not meant to be used production as this program has not benchmarked; you have been warned.

Install these packages from pip:<br>
`pip3 install pyftpdlib`<br>
`pip3 install setproctitle`<br>

Or you can run the following command:<br>
`pip3 install -r requirements.txt`<br>

If you don't have `pip` installed, install it via your package manager for painless installation.

### Docker

Build the image:<br>
`docker build -t lftpd .`<br>

Then, run the image:<br>
`docker run -p 21:21 lftpd`<br>

To fully stop the container, press Control + C to quit the container.
Then, stop the container by running the following command:<br>
`docker stop <container name or ID>`<br>
Replace 'container name or ID' with the actual name or ID of the container. You can obtain this by running the follwing command:<br>
`docker ps`<br>

## Running
Running is very simple:
`python3 ftpserver.py`

No flags and no extensions! I will add extensions once this FTP server becomes more mature and more stable.

Use a FTP client like Filezilla to test this.

## Troubleshooting
As far as I know, you didn't install something correctly. Make sure you installed everything. If nothing works, email me.

## Contributions
They are always welcome! Email me or send in a PR.
