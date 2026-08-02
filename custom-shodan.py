#!/usr/bin/env python3

import json
import os
import sys
import requests

# -------------------------------------------------
# Configuration
# -------------------------------------------------

SHODAN_API_KEY = os.getenv("Your Api Key")

pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_FILE = f"{pwd}/logs/integrations.log"


def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")


def extract_ip(alert):
    """
    Extract IP address from different Wazuh alert formats.
    """

    # Source IP
    if alert.get("data", {}).get("srcip"):
        return alert["data"]["srcip"]

    # Destination IP
    if alert.get("data", {}).get("dstip"):
        return alert["data"]["dstip"]

    # Agent IP
    if alert.get("agent", {}).get("ip"):
        return alert["agent"]["ip"]

    # Windows Event
    if alert.get("data", {}).get("win", {}).get("eventdata", {}).get("ipAddress"):
        return alert["data"]["win"]["eventdata"]["ipAddress"]

    return None  



def shodan_lookup(ip):
      if not SHODAN_API_KEY:
        return {
            "error": "Missing SHODAN_API_KEY environment variable"
        }

    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"

    try:
        response = requests.get(url, timeout=15)

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }

    # ----------------------------
    # Success
    # ----------------------------
    if response.status_code == 200:

        data = response.json()

        return {
            "status": "success",
            "ip": ip,
            "organization": data.get("org"),
            "isp": data.get("isp"),
            "country": data.get("country_name"),
            "city": data.get("city"),
            "operating_system": data.get("os"),
            "ports": data.get("ports"),
            "hostnames": data.get("hostnames")
        }

    # ----------------------------
    # Membership Required
    # ----------------------------
    elif response.status_code == 403:

        return {
            "status": "membership_required",
            "ip": ip,
            "message": "Shodan Membership or higher is required for this lookup."
        }

    # ----------------------------
    # IP not found
    # ----------------------------
    elif response.status_code == 404:

        return {
            "status": "not_found",
            "ip": ip,
            "message": "IP not found in Shodan database."
        }

    # ----------------------------
    # Other errors
    # ----------------------------
    else:

        return {
            "status": "error",
            "http_status": response.status_code,
            "body": response.text
        }


def main(args):

    if not SHODAN_API_KEY:
        log("ERROR: SHODAN_API_KEY environment variable is not set.")
        sys.exit(1)

    if len(args) < 2:
        log("ERROR: Alert file missing.")
        sys.exit(1)

    alert_file = args[1]

    try:
        with open(alert_file) as f:
            alert = json.load(f)

    except Exception as e:
        log(f"ERROR reading alert file: {e}")
        sys.exit(1)

    ip = extract_ip(alert)

    if not ip:
        log("No IP address found in alert.")
        sys.exit(0)

    result = shodan_lookup(ip)

    log(json.dumps(result))


if __name__ == "__main__":
    main(sys.argv)
