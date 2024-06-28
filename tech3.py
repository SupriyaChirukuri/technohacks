

import os
import subprocess

# Function to run a Linux command and print the output
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

# Step 1: Practice Linux Commands
commands = [
    "pwd",                    # Print working directory
    "ls -la",                 # List files in detail
    "uname -a",               # System information
    "whoami",                 # Current user
    "df -h",                  # Disk usage
    "free -m",                # Memory usage
    "ps aux",                 # Running processes
    "ifconfig",               # Network interfaces
    "netstat -tuln",          # Network connections
]

print("=== Practicing Basic to Advanced Linux Commands ===")
for cmd in commands:
    print(f"Running command: {cmd}")
    run_command(cmd)

# Step 2: Install Kali Linux Tools from GitHub
tools = [
    "https://github.com/sqlmapproject/sqlmap",  # SQL injection tool
    "https://github.com/OWASP/joomscan",        # Joomla vulnerability scanner
]

print("\n=== Installing Kali Linux Tools from GitHub ===")
for tool in tools:
    tool_name = tool.split('/')[-1]
    if not os.path.exists(tool_name):
        run_command(f"git clone {tool}")
    else:
        print(f"{tool_name} already exists")

# Step 3: Set Up Local Environment for Legal Penetration Testing
docker_compose_content = """
version: '2'
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "80:80"
"""

docker_compose_file = "docker-compose.yml"

print("\n=== Setting Up Local Environment for Legal Penetration Testing ===")
if not os.path.exists(docker_compose_file):
    with open(docker_compose_file, 'w') as file:
        file.write(docker_compose_content)
    run_command("docker-compose up -d")
else:
    print(f"{docker_compose_file} already exists")

print("\nSetup Complete. Access DVWA at http://localhost:80")
