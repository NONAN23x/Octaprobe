import requests
import os
import time
import pandas as pd

def virustotal_analysis(file_path):
        
        api_key = os.getenv("VIRUSTOTAL_API_KEY")
        # if not api_key:
        #     print("VirusTotal API key not found. Please set the 'VIRUSTOTAL_API_KEY' environment variable.")
        #     print("Visit https://www.virustotal.com/gui/my-apikeys for more information.")
        #     return
        
        url = "https://www.virustotal.com/api/v3/files"

        files = { "file": (file_path, open(f"{file_path}", "rb")) }
        headers = {
            "accept": "application/json",
            "x-apikey": api_key
        }

        response = requests.post(url, files=files, headers=headers)
        time.sleep(5)
        if response.status_code == 200:
            result = response.json()
            analysis_url = result.get("data", {}).get("links", {}).get("self")
            if analysis_url:

                start_time = time.time()
                while True:
                    analysis_response = requests.get(analysis_url, headers=headers)
                    status = analysis_response.json().get("data", {}).get("attributes", {}).get("status")
                    if status == "completed":
                        break
                    if time.time() - start_time > 30:
                        print("Analysis timed out after 35 seconds.")
                        break
                    print(f"Analysis status: {status}. Waiting for completion...")
                    time.sleep(5)  # Wait for 5 seconds
                elapsed_time = (time.time() - start_time)
                analysis_response = requests.get(analysis_url, headers=headers)
                
                if analysis_response.status_code == 200:
                    analysis_result = analysis_response.json()
                    hashes = analysis_result.get("meta", {}).get("file_info", {})
                    meta_data = {
                        "status": analysis_result.get("data", {}).get("attributes", {}).get("status"),
                        # "meta": analysis_result.get("meta", {})
                    }
                    stats = analysis_result.get("data", {}).get("attributes", {}).get("stats", {})
                    df = pd.DataFrame(list(stats.items()), columns=["Status", "Count"]).set_index("Status")
                    
                    return meta_data, df, hashes, elapsed_time
                    # return analysis_result
                else:
                    print(f"Failed to fetch analysis results. Status code: {analysis_response.status_code}")
                    return analysis_response.json()
            else:
                print("Analysis URL not found in the response. Is your inernet and API connection working?")
                return result
        
        else:
            print(f"Failed to upload file to VirusTotal. Status code: {response.status_code}")
            return(response.json())