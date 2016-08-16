import paramiko
from glob import glob
from scp import SCPClient
import pprint


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.__client__ = paramiko.SSHClient()
        self.__client__.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client__.connect(hostname=host, username=user, password=password)

    def close(self):
        try:
            self.__client__.close()
        except Exception as ex:
            print(ex)

    def move(self, source, destination):
        with SCPClient(self.__client__.get_transport()) as scp:
            for input_filename in glob(source):
                print("{0}: Moving {1} to {2}".format(self.host, input_filename, destination))
                scp.put(files=input_filename, remote_path=destination)

    def command(self, commands):
        pp = pprint.PrettyPrinter(indent=4)
        for command in commands:
            print("{0}: Running Shell: {1}".format(self.host, command))
            stdin, stdout, stderr = self.__client__.exec_command(command, bufsize = 2000)
            status_code = stdout.channel.recv_exit_status()
            output = stdout.readlines()
            pp.pprint(output)
            return status_code, output
