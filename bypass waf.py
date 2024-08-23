import requests

def doh_query(domain, dns_server="https://test-dns.com/dns-query"):
    headers = {
        'accept': 'application/dns-json'
    }
    
    response = requests.get(f"{dns_server}?name={domain}&type=A", headers=headers)
    
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Query failed with status code {response.status_code}")

# Example usage
doh_query("xxxxx.com")
