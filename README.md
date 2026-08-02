# 🛡️ Wazuh Threat Intelligence Integration using Shodan API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-green)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

This project demonstrates the integration of the **Shodan API** with **Wazuh SIEM** to enrich security alerts with external threat intelligence.

Whenever Wazuh generates a security alert, the custom Python integration automatically queries the Shodan API for additional information about the detected IP address. The retrieved intelligence can help security analysts gain better visibility into potentially malicious hosts.

This project provides a practical example of **Security Operations Center (SOC) automation** using **Python**, **Linux**, and **Wazuh SIEM**.

---

# ✨ Features

- Custom Wazuh Integration
- Shodan API Integration
- Automated Threat Intelligence Enrichment
- Python Automation
- Integration Logging
- Error Handling
- Easy Deployment
- Beginner Friendly

---

# 🛠 Technologies Used

- Wazuh SIEM
- Python 3
- Shodan API
- Linux
- JSON
- XML
- Git
- GitHub

---

# 📂 Project Structure

```text
Wazuh-Shodan-Integration/
│
├── custom-shodan.py
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── installation.md
│   ├── configuration.md
│   ├── testing.md
│   └── troubleshooting.md
│
└── screenshots/
    ├── dashboard.png
    ├── ossec-conf.png
    ├── integrations-log.png
    ├── alert.png
    └── shodan-response.png
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/spark077-code/Wazuh-Shodan-Integration.git
```

Move into the project

```bash
cd Wazuh-Shodan-Integration
```

Copy the integration script to the Wazuh integrations directory.

Edit the **ossec.conf** file and configure the integration.

Restart the Wazuh Manager.

```bash
sudo systemctl restart wazuh-manager
```

---

# ⚙️ Configuration

Edit the following configuration file:

```text
/var/ossec/etc/ossec.conf
```

Add the required integration block according to the project documentation.

Restart the Wazuh Manager after saving the configuration.

---

# 🧪 Testing

Generate a security alert from a monitored endpoint.

Verify that:

- Wazuh executes the custom integration.
- integrations.log records the execution.
- The Shodan API request is sent successfully.
- Alert enrichment is completed.

Example command:

```bash
tail -f /var/ossec/logs/integrations.log
```

---

# 📸 Project Screenshots

The repository includes screenshots demonstrating the complete integration workflow.

- Wazuh Dashboard
- ossec.conf Configuration
- Integration Log
- Triggered Alert
- Shodan API Response

> Screenshots will be added after completing the lab.

---

# 📈 Future Improvements

- VirusTotal Integration
- AbuseIPDB Integration
- GeoIP Enrichment
- Slack Notifications
- Email Notifications
- IOC Correlation
- Multiple Threat Intelligence Sources

---

# 🎯 Learning Objectives

Through this project you will learn:

- Wazuh Custom Integrations
- Python Automation
- API Integration
- Threat Intelligence
- SIEM Fundamentals
- Linux Administration
- SOC Workflow
- Security Alert Enrichment

---

# 📜 License

This project is licensed under the MIT License.

See the LICENSE file for more details.

---

# 👨‍💻 Author

**Faisal Mehmood**

Cybersecurity Enthusiast

SOC Analyst (Learning)

Blue Team • Threat Intelligence • Wazuh • Python • Linux

---

⭐ If you found this project useful, consider giving it a Star on GitHub.
