 # 🚀 Cisco Ansible & Python Automation Project

## 📌 Overview
This project demonstrates network automation and configuration management using **Cisco Modeling Labs (CML), Ansible, and Python**.  
It automates **router backups, retrieves configurations, and parses data** to generate meaningful reports.

---

## 🚩 Technologies Used
- **Cisco Modeling Labs (CML)**
- **Ansible** (for configuration automation)
- **Python** (for script-based automation)
- **Ubuntu VM** (for running automation tools)

---

## 📸 Project Demonstration
### 🔹 **1. Cisco CML Lab Topology**
This diagram represents the network setup used for automation.  
![image](https://github.com/user-attachments/assets/e01c1e09-8704-43f4-8ed6-059f8a1b4fec)

### 🔹 **2. SSH Connectivity Testing**
This confirms SSH access to network devices, ensuring Ansible and Python can execute commands remotely.
![image](https://github.com/user-attachments/assets/85c21074-8ec0-45ad-b432-7aad692bba3d)

### 🔹 **3. Ansible Playbook Execution (Backup)**
The Ansible playbook automatically backs up router configurations. 
![image](https://github.com/user-attachments/assets/83489ede-a00e-4f8f-9b31-598061d0b31b)

### 🔹 **4. Python Script Parsing Output**
A Python script extracts key details from router configs for reporting. 
![image](https://github.com/user-attachments/assets/290ff6a2-0c4f-4b96-a859-e7218271aa34)

---
## 🔧 Setup & Execution

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/NetEngSam/Cisco-Ansible-Python-Lab.git
cd Cisco-Ansible-Python-Lab
```
### 2️⃣ Install Dependencies
Ensure you have Ansible and Python installed:
```bash
sudo apt update && sudo apt install -y ansible python3 python3-pip
pip install paramiko netmiko
```
### 3️⃣ Configure Ansible Inventory
Edit inventory.yml with your router details:
```yml
[routers]
r1 ansible_host=192.168.1.6 ansible_user=cisco ansible_password=cisco
r2 ansible_host=10.0.12.2 ansible_user=cisco ansible_password=cisco
```
### 4️⃣ Run the Ansible Playbook
Execute the playbook to back up router configs:
```bash
ansible-playbook backup.yml
```
### 5️⃣ Run the Python Script
Use Python to parse the config and extract key details:
```bash
python3 parse_backups.py
```











