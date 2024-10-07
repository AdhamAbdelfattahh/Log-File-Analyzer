import re
from collections import Counter

def analyze_log(file_name):
    with open(file_name, 'r') as file:
        logs = file.readlines()

    suspicious_activity = []
    
    for line in logs:
        if "failed login" in line.lower():
            suspicious_activity.append(line)
        if "access denied" in line.lower():
            suspicious_activity.append(line)

    return suspicious_activity

def main():
    file_name = input("Enter the log file name: ")
    suspicious_activity = analyze_log(file_name)
    
    if suspicious_activity:
        print("Suspicious Activity Found:")
        for activity in suspicious_activity:
            print(activity.strip())
    else:
        print("No suspicious activity found.")

if __name__ == "__main__":
    main()
