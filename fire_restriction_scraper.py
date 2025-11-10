import sys
import urllib.request
import re

url = "https://www.cfa.vic.gov.au/warnings-restrictions/fire-danger-period/fire-restriction-dates"
try:
    html = urllib.request.urlopen(url).read().decode("utf-8", errors="ignore")
except Exception as e:
    print("Error fetching page")
    sys.exit(0)

# --- Read arguments ---
municipality = sys.argv[1] if len(sys.argv) > 1 else "Hepburn"
arg = sys.argv[2].lower() if len(sys.argv) > 2 else "both"

# --- Regex: substitute municipality ---
pattern = rf"<tr[^>]*>.*?<td[^>]*>\s*{re.escape(municipality)}\s*</td>(.*?)</tr>"
row_match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)

start_date = "No restrictions"
end_date = "No restrictions"

if row_match:
    row_rest = row_match.group(1)
    cells = re.findall(r"<td[^>]*>(.*?)</td>", row_rest, flags=re.IGNORECASE)
    cell_text = " ".join(cells)
    cell_text_clean = re.sub(r"<[^>]+>", " ", cell_text)
    cell_text_clean = re.sub(r"\s+", " ", cell_text_clean).strip()

    dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", cell_text_clean)
    if len(dates) >= 2:
        start_date, end_date = dates[0], dates[1]

# --- Output based on arg ---
if arg == "start":
    print(start_date)
elif arg == "end":
    print(end_date)
else:
    print(f"{start_date}|{end_date}")

sys.exit(0)
