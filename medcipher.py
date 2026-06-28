```python id="x8f2na"
import os
import json
import time
import socket
import random
import hashlib
import threading
from datetime import datetime


# ==================================================
# SECURITY LOGGER
# ==================================================

class SecurityLogger:

    def __init__(self):

        self.logs = []

    def log(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = f"[{timestamp}] [{level}] {message}"

        self.logs.append(entry)

        print(entry)

    def export_logs(self):

        with open("security_logs.json", "w") as file:

            json.dump(self.logs, file, indent=4)

        print("\n[EXPORT] Security logs exported.\n")


# ==================================================
# MEDICAL RECORD
# ==================================================

class MedicalRecord:

    def __init__(self, patient_id, name, disease):

        self.patient_id = patient_id

        self.name = name

        self.disease = disease

        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.encrypted = False

        self.record_hash = self.generate_hash()

    def generate_hash(self):

        raw = f"{self.patient_id}{self.name}{self.disease}"

        return hashlib.sha256(raw.encode()).hexdigest()

    def encrypt(self):

        self.encrypted = True

    def display(self):

        status = "ENCRYPTED" if self.encrypted else "UNPROTECTED"

        print(f"""
==================================================
Patient ID       : {self.patient_id}
Patient Name     : {self.name}
Disease           : {self.disease}
Created At        : {self.created_at}
Encryption Status : {status}
Record Hash       : {self.record_hash[:35]}...
==================================================
""")


# ==================================================
# DATABASE ENGINE
# ==================================================

class DatabaseEngine:

    def __init__(self):

        self.records = []

    def add_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records

    def encrypt_all(self):

        for record in self.records:

            record.encrypt()


# ==================================================
# AI THREAT ENGINE
# ==================================================

class AIThreatEngine:

    threat_levels = ["LOW", "MEDIUM", "HIGH"]

    def analyze(self):

        typing_behavior = random.randint(1, 100)

        session_behavior = random.randint(1, 100)

        access_pattern = random.randint(1, 100)

        anomaly_score = (
            typing_behavior +
            session_behavior +
            access_pattern
        ) // 3

        if anomaly_score < 40:

            level = "LOW"

        elif anomaly_score < 75:

            level = "MEDIUM"

        else:

            level = "HIGH"

        return {
            "level": level,
            "score": anomaly_score,
            "typing": typing_behavior,
            "session": session_behavior,
            "access": access_pattern
        }


# ==================================================
# NETWORK MONITOR
# ==================================================

class NetworkMonitor:

    suspicious_ports = [22, 21, 445, 3389]

    def scan(self):

        detected = []

        for port in self.suspicious_ports:

            if random.choice([True, False]):

                detected.append(port)

        return detected


# ==================================================
# ATTACK SIMULATOR
# ==================================================

class AttackSimulator:

    attacks = [

        "Unauthorized database access",
        "Potential ransomware execution",
        "Abnormal behavioral pattern",
        "Medical file exfiltration attempt",
        "Suspicious remote connection",
        "Privilege escalation attempt",
        "Brute force authentication activity",
        "Malicious packet stream detected"

    ]

    def generate_attack(self):

        return random.choice(self.attacks)


# ==================================================
# LIVE EVENT STREAM
# ==================================================

class EventStreamer:

    def __init__(self, logger):

        self.logger = logger

        self.running = False

    def start_stream(self):

        self.running = True

        def stream():

            while self.running:

                fake_events = [

                    "Streaming security telemetry...",
                    "Behavioral analytics active...",
                    "Monitoring network packets...",
                    "AI threat engine processing...",
                    "SOC dashboard synchronized...",
                    "Medical database integrity verified..."

                ]

                event = random.choice(fake_events)

                self.logger.log("STREAM", event)

                time.sleep(5)

        thread = threading.Thread(target=stream)

        thread.daemon = True

        thread.start()

    def stop_stream(self):

        self.running = False


# ==================================================
# MAIN PLATFORM
# ==================================================

class MedCipherAI:

    def __init__(self):

        self.logger = SecurityLogger()

        self.database = DatabaseEngine()

        self.ai = AIThreatEngine()

        self.network = NetworkMonitor()

        self.attacks = AttackSimulator()

        self.streamer = EventStreamer(self.logger)

    def create_record(self):

        patient_id = input("Patient ID: ")

        name = input("Patient Name: ")

        disease = input("Disease: ")

        record = MedicalRecord(
            patient_id,
            name,
            disease
        )

        self.database.add_record(record)

        self.logger.log(
            "INFO",
            f"Medical record created for {name}"
        )

    def display_records(self):

        records = self.database.get_records()

        if not records:

            self.logger.log(
                "WARNING",
                "No medical records found"
            )

            return

        for record in records:

            record.display()

    def encrypt_database(self):

        self.logger.log(
            "SECURE",
            "Encrypting medical database..."
        )

        time.sleep(2)

        self.database.encrypt_all()

        self.logger.log(
            "SECURE",
            "Database encryption completed"
        )

    def run_ai_detection(self):

        self.logger.log(
            "AI",
            "Running behavioral analysis engine..."
        )

        time.sleep(2)

        result = self.ai.analyze()

        print(f"""
================ AI THREAT ANALYSIS ================

Threat Level        : {result['level']}
AI Confidence Score : {result['score']}%

Typing Analysis     : {result['typing']}%
Session Analysis    : {result['session']}%
Access Pattern      : {result['access']}%

====================================================
""")

        if result["level"] == "HIGH":

            self.logger.log(
                "ALERT",
                "Critical anomaly detected"
            )

        elif result["level"] == "MEDIUM":

            self.logger.log(
                "WARNING",
                "Suspicious behavior identified"
            )

        else:

            self.logger.log(
                "SAFE",
                "No anomalies detected"
            )

    def simulate_attack(self):

        attack = self.attacks.generate_attack()

        self.logger.log(
            "ATTACK",
            attack
        )

    def monitor_network(self):

        self.logger.log(
            "NETWORK",
            "Scanning network infrastructure..."
        )

        time.sleep(2)

        suspicious = self.network.scan()

        if suspicious:

            for port in suspicious:

                self.logger.log(
                    "THREAT",
                    f"Suspicious port activity detected on port {port}"
                )

        else:

            self.logger.log(
                "SAFE",
                "No suspicious network activity detected"
            )

    def system_information(self):

        hostname = socket.gethostname()

        ip_address = socket.gethostbyname(hostname)

        print(f"""
================ SYSTEM INFORMATION ================

Hostname     : {hostname}
IP Address   : {ip_address}
Platform     : MedCipher AI Enterprise
Status       : OPERATIONAL

====================================================
""")

    def dashboard(self):

        self.streamer.start_stream()

        while True:

            print("""
==================================================
         MEDCIPHER AI ENTERPRISE PLATFORM
==================================================

1. Create Medical Record
2. Display Medical Records
3. Encrypt Medical Database
4. Run AI Threat Detection
5. Simulate Cyber Attack
6. Monitor Network Activity
7. View System Information
8. Export Security Logs
9. Exit Platform

==================================================
""")

            choice = input("Select option: ")

            if choice == "1":

                self.create_record()

            elif choice == "2":

                self.display_records()

            elif choice == "3":

                self.encrypt_database()

            elif choice == "4":

                self.run_ai_detection()

            elif choice == "5":

                self.simulate_attack()

            elif choice == "6":

                self.monitor_network()

            elif choice == "7":

                self.system_information()

            elif choice == "8":

                self.logger.export_logs()

            elif choice == "9":

                self.streamer.stop_stream()

                print("\n[SYSTEM] Shutting down platform...\n")

                break

            else:

                print("\n[ERROR] Invalid option.\n")


# ==================================================
# PLATFORM STARTUP
# ==================================================

platform = MedCipherAI()

platform.dashboard()
```
