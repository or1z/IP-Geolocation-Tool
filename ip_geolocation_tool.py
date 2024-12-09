import requests
import json
import os
import platform
import time
import sys

currency_symbols = {
    "USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "AUD": "A$", "CAD": "C$", "INR": "₹", "CNY": "¥", "MXN": "$", 
    "BRL": "R$", "RUB": "₽", "ZAR": "R", "CHF": "CHF", "SEK": "kr", "NOK": "kr", "DKK": "kr", "SGD": "S$", "HKD": "HK$", 
    "MYR": "RM", "THB": "฿", "IDR": "Rp", "KRW": "₩", "PHP": "₱", "TRY": "₺", "VND": "₫", "ILS": "₪", "CLP": "$", 
    "COP": "$", "PEN": "S/."
}

def get_ip_info(ip):
    url = f'http://ip-api.com/json/{ip}?fields=country,regionName,city,zip,lat,lon,isp,org,as,timezone,currency,query,continent,mcc,mnc,location_accuracy,connection_type,proxy,language,elevation,ip_type'
    response = requests.get(url)
    data = response.json()
    return data

def format_currency(currency_code):
    symbol = currency_symbols.get(currency_code, "")
    return f"{currency_code} - {symbol}" if symbol else currency_code

def clear_terminal():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_ip_info(data):
    user_name = os.getlogin()
    print(f"Welcome, {user_name}! This IP tool was made by github.com/or1z\n")
    
    col_width = 50
    row1 = f"{'IP Address:':<20} {data.get('query', 'N/A'):<{col_width}} {'Country:':<20} {data.get('country', 'N/A')}"
    row2 = f"{'Region:':<20} {data.get('regionName', 'N/A'):<{col_width}} {'City:':<20} {data.get('city', 'N/A')}"
    row3 = f"{'ZIP Code:':<20} {data.get('zip', 'N/A'):<{col_width}} {'Latitude:':<20} {data.get('lat', 'N/A')}"
    row4 = f"{'Longitude:':<20} {data.get('lon', 'N/A'):<{col_width}} {'Timezone:':<20} {data.get('timezone', 'N/A')}"
    
    currency = data.get('currency', 'N/A')
    formatted_currency = format_currency(currency)
    row5 = f"{'Currency:':<20} {formatted_currency:<{col_width}} {'ISP:':<20} {data.get('isp', 'N/A')}"
    
    row6 = f"{'Organization:':<20} {data.get('org', 'N/A'):<{col_width}} {'AS:':<20} {data.get('as', 'N/A')}"
    row7 = f"{'Continent:':<20} {data.get('continent', 'N/A'):<{col_width}} {'MCC:':<20} {data.get('mcc', 'N/A')}"
    row8 = f"{'MNC:':<20} {data.get('mnc', 'N/A'):<{col_width}} {'Location Accuracy (km):':<20} {data.get('location_accuracy', 'N/A')}"
    row9 = f"{'Connection Type:':<20} {data.get('connection_type', 'N/A'):<{col_width}} {'Proxy:':<20} {data.get('proxy', 'N/A')}"
    row10 = f"{'Language:':<20} {data.get('language', 'N/A'):<{col_width}} {'Elevation (meters):':<20} {data.get('elevation', 'N/A')}"
    row11 = f"{'IP Type:':<20} {data.get('ip_type', 'N/A'):<{col_width}}"

    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print(row8)
    print(row9)
    print(row10)
    print(row11)

def loading_animation():
    loading_text = "Loading"
    animation = ["|", "/", "-", "\\"]
    sys.stdout.write("\nPlease wait while we gather the information...\n")
    sys.stdout.flush()
    
    for i in range(20):
        sys.stdout.write("\r" + loading_text + " " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    while True:
        ip = input("\nInput an IP address or type exit to terminate the program: ")
        if ip.lower() == 'exit':
            print("Goodbye!")
            break
        
        clear_terminal()

        loading_animation()

        data = get_ip_info(ip)
        
        if data.get('status') == 'fail':
            print("Error: Invalid IP address or unable to retrieve information.")
        else:
            clear_terminal()
            print_ip_info(data)
        
        input("\nPress any key to continue...")
        clear_terminal()

if __name__ == "__main__":
    main()
