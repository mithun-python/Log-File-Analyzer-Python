# Log File Analyzer
# This script analyzes a log file and generates a summary report

def analyze_logs():
    error_count = 0
    warning_count = 0
    info_count = 0

    # Open log file in read mode
    with open("logs.txt", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    # Write summary report
    with open("report.txt", "w") as report:
        report.write("LOG FILE ANALYSIS REPORT\n")
        report.write("------------------------\n")
        report.write(f"Total ERROR logs: {error_count}\n")
        report.write(f"Total WARNING logs: {warning_count}\n")
        report.write(f"Total INFO logs: {info_count}\n")

    print("Log analysis completed. Report generated successfully.")

# Run the function
analyze_logs()
