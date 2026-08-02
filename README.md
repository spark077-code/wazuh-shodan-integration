# Wazuh + Shodan Threat Intelligence Integration

## Overview

This project demonstrates a custom integration between **Wazuh SIEM** and the **Shodan API** to enrich security alerts with external threat intelligence.

When Wazuh generates an alert containing an IP address, the custom integration automatically queries Shodan and retrieves additional information such as:

- Organization
- Operating System
- ISP
- Country
- City
- Open Ports
- Hostnames

The enriched information is written to the Wazuh integration logs for further analysis.

> **Note:** This project was developed for educational and lab purposes.

---

## Features

- Custom Python integration for Wazuh
- Automatic IP extraction from alerts
- Shodan API lookup
- JSON formatted output
- Integration with Wazuh alert workflow
- Environment variable support for API key
- Secure API key handling

---

## Project Structure

```
wazuh-shodan-integration/
│
├── custom-shodan
├── custom-shodan.py
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
```

---

## Requirements

- Wazuh Manager
- Python 3
- Requests Library
- Shodan API Key
- Linux (Rocky Linux tested)

---

## Installation

Copy the integration files to:

```
/var/ossec/integrations/
```

Make the scripts executable:

```bash
chmod 750 custom-shodan
chmod 750 custom-shodan.py
```

Restart Wazuh:

```bash
systemctl restart wazuh-manager
```

---

## Configuration

Add the following integration block inside:

```
/var/ossec/etc/ossec.conf
```

```xml
<integration>
    <name>custom-shodan</name>
    <rule_id>2502</rule_id>
    <alert_format>json</alert_format>
</integration>
```

Restart Wazuh after saving the configuration.

---

## Environment Variable

Store the API key securely:

```bash
export SHODAN_API_KEY="YOUR_API_KEY"
```

The integration reads the key using:

```python
os.getenv("SHODAN_API_KEY")
```

---

## Testing

Trigger an alert containing an IP address.

Example log output:

```json
{
  "ip":"8.8.8.8",
  "organization":"Google LLC",
  "country":"United States",
  "ports":[53]
}
```

---

## Current Limitation

The free Shodan API returns:

```
HTTP 403
Requires membership or higher to access
```

This is an API subscription limitation—not a problem with the integration itself.

---

## Future Improvements

- VirusTotal Integration
- AbuseIPDB Integration
- AlienVault OTX Integration
- GeoIP Mapping
- Dashboard Visualization
- Multiple Threat Intelligence Sources

---

## Screenshots

Project screenshots will be added here.

---

## Author

**Faisal Mehmood**

Cyber Security Learner

GitHub:
https://github.com/spark077-code

---

## License

This project is released for educational purposes.