# cybersecurity_analysis_tools
## [Skills for Hire Atlantic Cybersecurity Program](https://skillsforhire.ca/programs/cyber-security/) Project, Fall 2023
 ---	

*Note: Part 4 uses a file called part4.file for malware analysis. This file is for educational purposes only.* 
### Part 1: Cryptography
For this part, I was required to use Python to perform some cryptography operations. After installing the necessary cryptographic modules, I verified the hash of the supplied files with their hashes. Next, I decrypted the encrypted text file using AES-128. Finally, I verified the plaintext using the provided signature and public key.

### Part 2: Log File Analysis
For this part, I had to analyze the provided log file. This file contained log entries from a Linux server over the course of a month. I opened the log file so that only a single line at a time was loaded into memory. I parsed the log file and recorded the highlighted fields, before creating a datetime object. Next, I found and printed the three most commonly used components and briefly described them. Finally, I created a plot that showed how these three common components were used throughout the day.

### Part 3: Network Scanning
I created a network scanner in Python, which attempted to discover all hosts within the network specified. The scanner operates in two different modes: one using ICMP echo packets and the other sending TCP SYN packets to a user-supplied port.

### Part 4: Malware Analysis
I performed analysis on a suspicious file. First, I installed the necessary modules to use YARA and analyze PE files. I used the supplied YARA rules to determine the type of file and used functions to check for any imports in the file. Then, I used different functions to analyze the sections of the file. Based on my findings, I identified three things that made the file suspicious.