import streamlit as st

def sheets():

    def linux_hardening_cheatsheet():
        checklist = {
            "🔒 Disable root SSH login": False,
            "🚪 Change default SSH port": False,
            "🧱 Enable UFW or iptables": False,
            "🔑 Enforce strong password policy": False,
            "🛑 Install fail2ban or equivalent": False,
            "🧹 Disable unused services": False,
            "📦 Keep OS packages up-to-date": False,
            "⚙️ Set up automatic security updates": False,
            "👮‍♂️ Restrict sudo access (use wheel/group)": False,
            "🗝️ Use SSH key authentication only": False,
            "📡 Disable ICMP (ping) response if needed": False,
            "📜 Enable auditd or journald logging": False,
            "🛡️ Protect /boot with read-only mount": False,
            "🔐 Enable AppArmor or SELinux": False,
            "🧾 Configure system-wide umask": False,
            "⏰ Limit cron/at usage to trusted users": False,
            "📁 Ensure correct file permissions in /etc": False,
            "🧨 Check for world-writable files": False,
            "🔍 Run a rootkit scanner (chkrootkit/rkhunter)": False,
            "🔎 Check for open ports with netstat/ss": False
        }

        completed = 0
        total = len(checklist)
        cols = st.columns(2)
        tasks = list(checklist.keys())
        for i, task in enumerate(tasks):
            col = cols[i % 2]  # Alternate between the two columns
            with col:
                if st.checkbox(task, key=task):
                    completed += 1
        progress = completed / total
        st.progress(progress)
        st.success(f"✅ {completed} of {total} tasks completed ({int(progress * 100)}%)")

    def windows_hardening_cheatsheet():
        checklist = {
            "🔒 Disable SMBv1": False,
            "🛡️ Enable Windows Defender": False,
            "🔑 Enforce strong password policy": False,
            "🚪 Disable guest account": False,
            "🧱 Enable Windows Firewall": False,
            "📦 Keep OS and software up-to-date": False,
            "🔍 Enable auditing and logging": False,
            "🛑 Disable unnecessary services": False,
            "🔐 Use BitLocker for disk encryption": False,
            "📜 Configure User Account Control (UAC)": False,
            "🗝️ Use local group policies for security settings": False,
            "📁 Set NTFS permissions correctly": False,
            "🧨 Check for weak passwords in user accounts": False,
            "🔎 Run a malware scanner regularly": False,
            "🛡️ Enable RDP Network Level Authentication": False,
            "🔒 Configure account lockout policy": False,
            "📜 Enable secure boot": False,
            "🧹 Remove unused user accounts": False,
            "🔍 Check for open ports with netstat": False,
            "🛠️ Apply security baselines (e.g., CIS)": False
        }
        completed = 0
        total = len(checklist)
        cols = st.columns(2)
        tasks = list(checklist.keys())
        for i, task in enumerate(tasks):
            col = cols[i % 2]
            with col:
                if st.checkbox(task, key=task):
                    completed += 1
        progress = completed / total
        st.progress(progress)
        st.success(f"✅ {completed} of {total} tasks completed ({int(progress * 100)}%)")

    def black_box_enumeration_cheatsheet():
        checklist = {
            "🔍 Identify target IP address": False,
            "🌐 Perform DNS enumeration": False,
            "📡 Scan for open ports": False,
            "🛠️ Identify running services and versions": False,
            "🔑 Check for default credentials": False,
            "🧩 Look for web applications": False,
            "📜 Review robots.txt and sitemap.xml": False,
            "🔍 Check for subdomains": False,
            "🧪 Test for SQL injection vulnerabilities": False,
            "🔒 Test for XSS vulnerabilities": False,
            "🔑 Test for CSRF vulnerabilities": False,
            "🔍 Check for sensitive files (e.g., .env)": False,
            "📂 Enumerate directories and files": False,
            "🔗 Check for insecure HTTP methods": False,
            "🛡️ Test for directory traversal vulnerabilities": False,
            "📄 Analyze HTTP headers for security issues": False,
            "🔍 Look for exposed admin panels": False,
            "🧪 Test for command injection vulnerabilities": False,
            "🔒 Check for weak SSL/TLS configurations": False,
            "📊 Perform vulnerability scanning with tools": False
        }
        completed = 0
        total = len(checklist)
        cols = st.columns(2)
        tasks = list(checklist.keys())
        for i, task in enumerate(tasks):
            col = cols[i % 2]  # Alternate between the two columns
            with col:
                if st.checkbox(task, key=task):
                    completed += 1
        
        progress = completed / total
        st.progress(progress)
        st.success(f"✅ {completed} of {total} tasks completed ({int(progress * 100)}%)")

    def webapp_security_cheatsheet():
        checklist = {
            "🔒 Implement HTTPS with a valid SSL certificate": False,
            "🛡️ Use secure headers (e.g., Content-Security-Policy)": False,
            "📜 Validate and sanitize user inputs": False,
            "🛡️ Use parameterized queries or ORM": False,
            "🔑 Enforce strong password policies for users": False,
            "🔒 Implement multi-factor authentication (MFA)": False,
            "🔑 Implement proper session management": False,
            "📜 Use secure cookie attributes (HttpOnly, Secure)": False,
            "🛡️ Protect against CSRF attacks": False,
            "🔒 Test for XSS vulnerabilities": False,
            "🧪 Test for SQL injection vulnerabilities": False,
            "🛡️ Protect against clickjacking (X-Frame-Options)": False,
            "📂 Restrict access to sensitive files and directories": False,
            "📂 Limit file upload types and sizes": False,
            "🛠️ Regularly update and patch dependencies": False,
            "🔍 Scan for vulnerabilities in third-party libraries": False,
            "🔍 Monitor and log security events": False,
            "🔍 Perform regular security audits": False,
            "📜 Ensure proper error handling and logging": False,
            "🔒 Use a Web Application Firewall (WAF)": False
        }
        completed = 0
        total = len(checklist)
        cols = st.columns(2)
        tasks = list(checklist.keys())
        for i, task in enumerate(tasks):
            col = cols[i % 2]  # Alternate between the two columns
            with col:
                if st.checkbox(task, key=task):
                    completed += 1
        
        progress = completed / total
        st.progress(progress)
        st.success(f"✅ {completed} of {total} tasks completed ({int(progress * 100)}%)")

    # Create two columns for layout
    col1, col2 = st.columns([0.9, 0.1])

    with col1:
        st.write("#### Useful Checklists to aid your security assessments!")
    
    with col2:
        with st.popover("💡"):
            st.write("These checklists are designed to help you identify potential security issues and improve the overall security posture of your systems.")
            st.warning("Fair usage notice: These checklists are provided for educational purposes only. Please ensure you have permission to conduct security assessments on any system or network.")


    checklist_options = {
        "Linux Hardening": linux_hardening_cheatsheet,
        "Windows Hardening": windows_hardening_cheatsheet,
        "Black Box Enumeration": black_box_enumeration_cheatsheet,
        "Web Application Security": webapp_security_cheatsheet,
        # Add more checklists here as needed
    }

    selected_checklist = st.selectbox("Select a Cheatsheet", list(checklist_options.keys()))

    if selected_checklist:
        checklist_options[selected_checklist]()