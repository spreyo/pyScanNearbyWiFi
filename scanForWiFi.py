import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(9)
results = iface.scan_results()
ssids = []

def deleteRepeating():
    for i in range(0, len(ssids)):
        try:
            if ssids[i] in ssids[0:i-1]:
                del ssids[i]
        except:
            pass

for i in results:
    ssid = i.ssid
    bssid = i.bssid
    ssids.append(f"{ssid}")

print(ssids)

deleteRepeating()

print(ssids)