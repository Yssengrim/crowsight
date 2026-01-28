# crowsight

Crowsight - Network Monitor (Python Home Lab)

A modular, Python-based network monitoring tool built for home lab environments to practice network discovery, performance diagnostics, and defensive security fundamentals.

This project focuses on visibility and troubleshooting, not exploitation, and is designed to grow incrementally as features and complexity are added.

Key Capabilities

Discovers active hosts on a local subnet

Measures host latency (ICMP)

Identifies common open ports (non-intrusive)

Persists scan results for historical comparison

Clean, extensible project architecture

Why This Project Exists

This project was built to:

Practice real-world Python networking concepts

Learn how monitoring tools are structured internally

Emphasize safe, authorized, read-only inspection

Serve as a foundation for future security and observability work

It mirrors how entry-level enterprise monitoring and asset discovery tools are designed—just at home-lab scale.

Architecture Overview
network_monitor/
│
├── main.py            # Orchestrates scans
├── config.py          # Centralized configuration
│
├── discovery.py       # Host discovery
├── latency.py         # Performance metrics
├── ports.py           # Limited port visibility
│
├── storage.py         # SQLite persistence
└── report.py          # Reporting (future)


Each module has a single responsibility, making the system easy to test, extend, and refactor.

Technologies Used

Python 3.11+

Standard library networking modules

SQLite for persistent storage

Designed to support future async and visualization tooling

No external dependencies are required for the initial phase.

Getting Started
Configure

Edit config.py to match your network:

SUBNET = "192.168.1.0/24"
PING_COUNT = 3
COMMON_PORTS = [22, 80, 443, 3389]
DB_FILE = "network.db"

Run
python main.py


The program discovers hosts, collects metrics, and stores results locally.

Data & Persistence

Each scan records:

Timestamp

IP address

Latency (ms)

Open ports (from a limited, predefined set)

This enables trend analysis and historical troubleshooting rather than one-off scans.

Ethical Use

Authorized networks only.

This tool is designed for:

Personal home labs

Learning environments

Networks where explicit permission is granted

It performs read-only diagnostics and does not attempt exploitation, credential access, or denial-of-service behavior.

Ethical Use & Disclaimer

⚠️ Authorized use only

This tool is intended only for:

Personal home labs

Networks you own

Networks where you have explicit permission to scan

The project performs read-only diagnostics and does not attempt exploitation, credential testing, or privilege escalation.

The author assumes no responsibility for misuse.
