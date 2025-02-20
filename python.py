import datetime

def main():
    now = datetime.datetime.now()
    message = f"Jenkins Job Executed Successfully on {now.strftime('%Y-%m-%d %H:%M:%S')}"
    print(message)
    
    # Write output to a log file
    with open("jenkins_output.log", "w") as log_file:
        log_file.write(message + "\n")

if __name__ == "__main__":
    main()
