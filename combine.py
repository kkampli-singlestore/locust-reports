# combine_iframe.py
combined_iframe_html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Combined Locust Report</title>
    <style>
      body { margin: 0; padding: 0; font-family: sans-serif; }
      iframe { width: 100%; height: 800px; border: none; margin-bottom: 20px; }
      h2 { padding: 10px; background: #f0f0f0; margin: 0; }
    </style>
  </head>
  <body>
    <h2>Locust Report: Gateway Tracking</h2>
    <iframe src="locust_report_gateway_tracking.html"></iframe>

    <h2>Locust Report: Gateway Without Container Tracking</h2>
    <iframe src="locust_report_gateway_1.html"></iframe>
  </body>
</html>
"""

with open("combined_gateway_iframe_report.html", "w") as f:
    f.write(combined_iframe_html)

print("✅ Created combined_gateway_iframe_report.html")
