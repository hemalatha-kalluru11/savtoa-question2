# Candidate ID: SAV116
# savtoa-question2
Savtoa Technologies Round2 Technical Assessment -Question2

# Collision Risk Monitoring System

This project is a small web-based system that shows how ships and nearby targets are monitored to detect possible collision risks.
It uses Python for simulation and HTML, CSS, and JavaScript for visualization.

The goal is to show:
  - Where targets are located
  - How risky each target is
  - Whether the situation is Safe, Warning, or Dangerous

# How the system works

1. A Python program generates random ship and target positions.
2. It calculates the CPA (Closest Point of Approach) for each target.
3. Based on the CPA value, the system decides:
    - Safe
    - Warning
    - Danger
4.This data is saved in a JSON file.
5.The web page reads this JSON file and displays:
    - Targets as dots on a map
    - Risk status in the alert panel

# Risk Levels
CPA Value         	Risk Level
Less than 10	        - Danger
Between 10 and 30     - Warning
More than 30          - Safe

# Technologies Used
Python
HTML
CSS
JavaScript

# How to run this project

1.Run the Python file to generate data:
  python stimulation.py
2.Start a local server:
  python -m http.server 8000
3.Open browser and go to: 
  http://localhost:8000/index.html

# Output

Targets appear as dots on the map
Alert panel shows each target with its CPA and risk status
Data updates continuously
