from config import *
from discovery import discover_hosts
from latency import measure_latency
from ports import check_ports
from storage import init_db, save_result

init_db(DB_FILE)

hosts = discover_hosts(SUBNET)

for host in hosts:
    latency = measure_latency(host)
    ports = check_ports(host, COMMON_PORTS)
    save_result(DB_FILE, host, latency, ports)

print("Scan complete.")
