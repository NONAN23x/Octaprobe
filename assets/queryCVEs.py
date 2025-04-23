import requests
import json
import os
import time

def fetch_cves():
    cache_file = os.path.join(os.getcwd(), "assets", "data", ".cve_cache.json")
    if not os.path.exists(cache_file):
        with open(cache_file, "w") as f:
            json.dump({"timestamp": 0, "cves": []}, f)
    current_time = time.time()

    # Check if cache exists and is valid
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cache_data = json.load(f)
            last_updated = cache_data.get("timestamp", 0)

        # If cache is less than 1 hours old, use it
        if current_time - last_updated < 1 * 60 * 60:
            cves = cache_data.get("cves", [])
            for cve in cves:
                result = [{"id": cve.get("cve_id"), 
                   "summary": cve.get("summary"), 
                   "published": cve.get("published_time")} 
                   for cve in cves]
                
            # print(result)
            return result

    # Fetch new data if cache is invalid or expired
    endpoint = "https://cvedb.shodan.io/cves"
    params = {
        "limit": 4
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    cves = data.get("cves", [])

    # Cache the data with timestamp
    with open(cache_file, "w") as f:
        json.dump({"timestamp": current_time, "cves": cves}, f)

    for cve in cves:
        result = [{"id": cve.get("cve_id"), 
                   "summary": cve.get("summary"), 
                   "published": cve.get("published_time")} 
                   for cve in cves]
        return result

