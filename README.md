# Mikrotik Router Configuration Tool

This program enables automated configuration of Mikrotik routers via SSH connection. It's specifically designed for integrating CCTV cameras on a local network with a cloud-based time-lapse shooting service using an installed router. The primary goal is to facilitate the quick setup of the SXT LTE6 kit for VPN use, addressing the challenge of fixed IP addresses on mobile operator networks.

## Features

- **Network Interfaces**: Configure the router's network interfaces for optimal performance.
- **Access Accounts**: Set up user access accounts securely.
- **Firewall**: Implement firewall settings to protect the network.
- **VPN Setup**: Install and configure VPN services to ensure secure and stable connections.

## Operating Modes

- **Manual Authorization**: Manually authenticate and configure settings.
- **Automatic Configuration**: Use a prepared configuration file for automated setup.

## Installation

Ensure you have Python 3.11 installed on your system. Then, follow these steps:

1. Clone the repository or download the program files to your local machine:
git clone https://github.com/TIMELAPSECENTER/mikrotik-ssh-updater

2. Navigate to the program directory and run:
mikrotik_setup.py

## Usage

To configure your Mikrotik router, use the following scripts:

- `mikrotik_setup.py`: Run this script through the console to manually set up the Mikrotik router.
- `mikrotik_setup.ini`: Place this configuration file in the same directory as the script for automatic configuration.
- `mikrotik.ovpn`: Includes the VPN key and configuration details. Ensure this file is properly configured for your VPN setup.

### Example Command

python mikrotik_setup.py
