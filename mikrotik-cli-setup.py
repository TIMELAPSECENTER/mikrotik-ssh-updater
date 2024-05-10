#!/usr/bin/env python3
import paramiko
import configparser
import click
import socket
from scp import SCPClient


def main():
    # Reading a Config File
    config = configparser.ConfigParser()
    config.read('mikrotik_setup.ini')

    manual_config = config.get('main', 'manual_config', fallback='1')
    router_ip = config.get('main', 'ip', fallback='192.168.1.98')
    router_port = config.get('main', 'port', fallback='22')
    router_username = config.get('main', 'username', fallback='admin')
    router_password = config.get('main', 'password', fallback='admin')
    router_password_new = config.get('main', 'password_new', fallback='timelapse-pass-2024')
    local_file = config.get('main', 'local_file', fallback='mikrotik.ovpn')
    remote_file = config.get('main', 'remote_file', fallback='mikrotik.ovpn')

    # If manual configuration is enabled, then request manual input
    if manual_config == "1":
        router_ip = input("IP: ")
        router_username = input("User: ")
        router_password = input("Password: ")

    # Check the connection to the router's IP address
    try:
        socket.inet_aton(router_ip)
        print(f"Connection to address {router_ip}")
    except socket.error:
        print(f"{router_ip} is not valid!")

    # Change password to router_password_new
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(router_ip, port=router_port, username=router_username, password=router_password)

        command = f"/user set 0 password={router_password_new}"
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())

        ssh_client.close()
    except:
        print(f"Authorization Failed!")

    # Create session with a new password
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(router_ip, port=router_port, username=router_username, password=router_password_new)

        # Copy the file mikrotik.ovpn to the router
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(local_file, remote_file)

        # Execute ssh commands =================================
        # Install keys from the mikrotik.ovpn configuration file
        command = "/certificate import file-name=mikrotik.ovpn"
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())

        # Establish a VPN connection
        command = "/interface ovpn-client add connect-to=vpn10.timelapse.center name=\"VPN\" port=1197 user=user disabled=no certificate=mikrotik.ovpn_1"
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())

        # Set up a firewall
        command = "/ip firewall filter disable number=5"
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())
        # ===================================================

        ssh_client.close()
    except:
        pass

    click.pause()


if __name__ == "__main__":
    main()
