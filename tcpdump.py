# Project specific modules
# from Common import logger
#Python specific modules
import subprocess

#logger = Logger.createLogger('tcpdump_log')

tcpdump_cmd = ['tcpdump','-w', '/c/Users/Matthew/Desktop/test.txt', '-l', '-c', '500']

try:
    p = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE)
except Exception as err:
    #  logger.error("[ERROR] saveTCPDump(): {}".format(err))
    print(err)
