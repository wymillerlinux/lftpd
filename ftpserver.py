import os
import sys
import logging
#import setproctitle
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import MultiprocessFTPServer

bindip = "0.0.0.0"
bindport = 21
isRunning = True

def FTPLogInfo(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('log_info.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(str(message))

def FTPLogWarn(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARN)
    handler = logging.FileHandler('log_warn.log')
    handler.setLevel(logging.WARN)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(message)

def FTPLogErr(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('log_err.log')
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(message)

def FTPLogCrit(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.CRITICAL)
    handler = logging.FileHandler('log_critical.log')
    handler.setLevel(logging.CRITICAL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(message)

class CustomHandler(FTPHandler):
    def on_connect(self):
        FTPLogInfo("%s:%s is now connected" % (self.remote_ip, self.remote_port))

class OperatingSystemError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def exitError(errorcode):
    print("[FATAL]: Exit error code ", errorcode)

def Interrupt():
    try:
        KeyboardInterrupt()
        sys.exit(0)
    except:
        KeyboardInterrupt(print("[INFO]: Server is going down gently!"))
        sys.exit(0)

if os.name == 'posix':
    authorizer = UnixAuthorizer()
# Trying to get Windows to work...
#elif os.name == 'nt':
#    authorizer = WindowsAuthorizer()
else:
    try:
        OperatingSystemError(print("[WARN]: Your operating system isn't supported! This software runs only on Unix machines!"))
    except OperatingSystemError:
        print("[WARN]: This shouldn't happen but alrighty then!")
        exitError(str(-1))
        sys.exit(0)

handler = FTPHandler
handler.authorizer = authorizer

while isRunning:

    #setproctitle.setproctitle("lftpd")
    FTPLogInfo(("Starting Lame FTP service on ", bindport))
    print("Press Ctrl-C to stop the servicing!")
    server = MultiprocessFTPServer((bindip, bindport), handler)
    server.serve_forever()

    if (Interrupt()):
        isRunning == False
        sys.exit(0)
