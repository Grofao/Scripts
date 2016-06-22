import argparse
from Client import Client


def run_on_all(args, operation):
    for ip_address in args.ip_address:
        client = Client(ip_address, args.user, args.password)
        operation(args, client)
        client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SSH Shell Runner')
    parser.add_argument("task", choices=['move_file', 'command'])
    parser.add_argument('-s', '--source', required=False, help='Target source')
    parser.add_argument('-d', '--destination', required=False, help='Target destination')
    parser.add_argument('-c', '--commands', nargs='+', required=False, help='Shell command')
    parser.add_argument('-ip', '--ip_address', nargs='+', help='Target IP address', required=True)
    parser.add_argument('-u', '--user', help='Username', required=True)
    parser.add_argument('-p', '--password', help='password', required=True)
    arguments = parser.parse_args()
    if arguments.task == "command":
        run_on_all(arguments, lambda a, c: c.command(a.commands))
    elif arguments.task == "move_file":
        run_on_all(arguments, lambda a, c: c.move(a.source, a.destination))
