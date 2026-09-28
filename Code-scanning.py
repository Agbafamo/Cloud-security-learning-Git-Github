import re

patterns = {
    "Hardcoded password": r'password\s*=\s*["\'].*["\']',
    "Hardcoded API key": r'api[_-]?key\s*=\s*["\'].*["\']',
    "Use of eval()": r'\beval\s*\(',
    "Use of exec()": r'\bexec\s*\(',
    "Use of subprocess": r'\bsubprocess\.',
    "SQL string concatenation": r'(SELECT|INSERT|UPDATE|DELETE).*\+',
}

def scan_file(filename):
    print(f"\nScanning: {filename}")
    print("-" * 50)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    findings = 0

    for line_number, line in enumerate(lines, start=1):
        for vulnerability, pattern in patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                print(f"[!] {vulnerability}")
                print(f"    Line {line_number}: {line.strip()}")
                findings += 1

    if findings == 0:
        print("[+] No matching insecure patterns found.")
    else:
        print(f"\n[!] Total findings: {findings}")


filename = input("Enter Python file to scan: ")
scan_file(filename)