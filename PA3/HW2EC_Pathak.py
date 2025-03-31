#File Name: HW2EC_Pathak.py
#Author: Shivam Pathak
#Date: 2.22.25
#Extra credit question
import math
import numpy as np

# Function to format numbers in scientific notation
def format_large_number(n):
    """Formats large numbers using scientific notation."""
    try:
        if n > 10**6:
            return f"{n:.5e}".replace('e+', ' x 10^')
        return str(n)
    except OverflowError:
        return "Too Large"

# Time limits in seconds
time_limits = {
    "1 second": 1,
    "1 minute": 60,
    "1 hour": 3600,
    "1 day": 86400,
    "1 month": 2592000,
    "1 year": 31536000,
    "1 century": 3153600000
}

# Complexity functions
complexities = [
    ("log(n)", lambda n: format_large_number(math.log(n)) if n > 1 else "N/A"),
    ("sqrt(n)", lambda n: format_large_number(math.sqrt(n))),
    ("n", lambda n: format_large_number(n)),
    ("n log(n)", lambda n: format_large_number(n * math.log(n)) if n > 1 else "N/A"),
    ("n^2", lambda n: format_large_number(n ** 2)),
    ("n^3", lambda n: format_large_number(n ** 3)),
    ("2^n", lambda n: format_large_number(np.power(2, n)) if n < 150 else f"2^({n})"),
    ("n!", lambda n: format_large_number(math.factorial(n)) if n < 150 else f"{n}!")
]

# Start HTML file
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Comparison of Running Times</title>
    <style>
        table { width: 80%; border-collapse: collapse; margin: 20px auto; }
        th, td { border: 1px solid black; padding: 10px; text-align: center; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2 style='text-align:center;'>Comparison of Running Times</h2>
    <table>
        <tr>
            <th>Time Limit</th>
"""

# Add headers
for label, _ in complexities:
    html_content += f"<th>{label}</th>"
html_content += "</tr>"

# Generate table rows
for label, n in time_limits.items():
    html_content += f"<tr><td>{label}</td>"
    for _, func in complexities:
        html_content += f"<td>{func(n)}</td>"
    html_content += "</tr>"

# Close table
html_content += """
    </table>
</body>
</html>
"""

# Write to file
with open("HW2ECResult_Pathak.html", "w") as file:
    file.write(html_content)

print("HTML file 'HW2ECResult_Pathak.html' generated successfully! Open it in a browser to view.")


