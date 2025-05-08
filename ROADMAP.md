# OctaProbe Project Roadmap

This document outlines the core development goals and planned features for the OctaProbe toolkit.

## ✅ Phase 1: Optimization & Codebase Polishing

- Improve performance and responsiveness of the Streamlit UI
- Refactor redundant or inefficient logic
- Optimize concurrent scanning mechanisms
- Polish UI consistency and error handling

## 🧾 Phase 2: Report Generation Feature

- Build a report generation module (`assets/report_gen.py`)
- Generate professional PDF reports of scan results
- Include, scan metadata, and summary tables
- Add download functionality from within the Streamlit interface

## 🗃️ Phase 3: Database Integration

- Integrate SQLite3 for storing scan data persistently
- Support viewing previous scans from the UI
- Enable querying and exporting historical scan data

## 🧮 Phase 4: Include CVSS Calculator

- Implement a CVSS (Common Vulnerability Scoring System) calculator
- Allow users to input vulnerability metrics
- Calculate and display CVSS scores dynamically
- Provide detailed breakdowns of the scoring process
- Integrate CVSS results into scan reports and database entries
- Add support for exporting CVSS calculations as JSON or CSV

## 🌐 Phase 5: Enhanced Port Scanner

- Upgrade the port scanning module for improved accuracy and speed
- Add support for scanning IPv6 addresses
- Implement service detection to identify applications running on open ports
- Include advanced scanning techniques (e.g., SYN scan, UDP scan)
- Provide detailed port status explanations in the scan results
- Integrate results with the report generation and database modules
- Add user-configurable scanning options (e.g., port ranges, timeout settings)
- Ensure compatibility with the CVSS calculator for detected vulnerabilities
---

**Note:** Please refer to this roadmap before submitting pull requests or proposing features. Contributions unrelated to the above items may be deferred or rejected.
