import re
import os
from collections import Counter

def extract_emails(lines):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return set(re.findall(email_pattern, "\n".join(lines)))

def extract_ips(lines):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ip_pattern, "\n".join(lines))

def count_ip_occurrences(ips):
    return Counter(ips)

def extract_timestamps(lines):
    timestamp_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'
    return re.findall(timestamp_pattern, "\n".join(lines))

def extract_timestamps_with_ips(lines):
    timestamp_pattern = r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b'
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    results = []
    for line in lines:
        timestamp_match = re.search(timestamp_pattern, line)
        ip_match = re.search(ip_pattern, line)
        if timestamp_match:
            timestamp = timestamp_match.group()
            ip = ip_match.group() if ip_match else "No IP"
            results.append(f"{timestamp} - {ip}")
    
    return results

def search_keyword(lines, keyword):
    return [line for line in lines if keyword in line]

def search_custom_regex(lines, custom_pattern):
    try:
        pattern = re.compile(custom_pattern)
        return [line for line in lines if pattern.search(line)]
    except re.error:
        print("Invalid regular expression.")
        return []

def extract_full_log_entries(lines, search_term):
    """ Extracts full log entries based on IP, timestamp, or keyword """
    return [line.strip() for line in lines if search_term in line]

def analyze_logs():
    file_path = input("Enter the log file name or path: ")
    
    if not os.path.exists(file_path):
        print("File not found. Make sure it's in the same directory or provide the full path.")
        return
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error opening file: {e}")
        return
    
    while True:
        print("\n--- Log Analyzer Menu ---")
        print("1. Search by keyword")
        print("2. Extract all emails")
        print("3. Extract all IPs")
        print("4. Count IP occurrences")
        print("5. Extract timestamps with IPs")
        print("6. Extract full log entries by IP, timestamp, or keyword")
        print("7. Search by custom regex")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ")
        
        if choice == "1":
            keyword = input("Enter the keyword to search: ")
            matches = search_keyword(lines, keyword)
            print("\n".join(matches) if matches else "No matches found.")
        elif choice == "2":
            emails = extract_emails(lines)
            print("\n".join(emails) if emails else "No emails found.")
        elif choice == "3":
            ips = extract_ips(lines)
            print("\n".join(set(ips)) if ips else "No IPs found.")
        elif choice == "4":
            ips = extract_ips(lines)
            ip_counts = count_ip_occurrences(ips)
            for ip, count in ip_counts.items():
                print(f"{ip}: {count} times")
        elif choice == "5":
            timestamps = extract_timestamps_with_ips(lines)
            print("\n".join(timestamps) if timestamps else "No timestamps found.")
        elif choice == "6":
            search_term = input("Enter IP, timestamp, or keyword: ")
            log_entries = extract_full_log_entries(lines, search_term)
            print("\n".join(log_entries) if log_entries else "No log entries found.")
        elif choice == "7":
            custom_pattern = input("Enter the custom regex pattern: ")
            matches = search_custom_regex(lines, custom_pattern)
            print("\n".join(matches) if matches else "No matches found.")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    analyze_logs()
