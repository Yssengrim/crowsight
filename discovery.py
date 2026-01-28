import ipaddress
import subprocess

def discover_hosts(subnet):
    active_hosts = []

    for ip in ipaddress.ip_network(subnet):
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stdout=subprocess.DEVNULL
        )
        if result.returncode == 0:
            active_hosts.append(str(ip))

    return active_hosts

