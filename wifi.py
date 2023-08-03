import subprocess
import time

print ("Turning on you wifi hacker")
for pause_in_secound in [3]:
    time.sleep(pause_in_secound)
print("utilities.....")
#sleep fun 3 sec
for pause_in_secound in [3]:
    time.sleep(pause_in_secound)
print("everything stisfied ......")
for pause_in_secound in [3]:
    time.sleep(pause_in_secound)
#sleep fun 3 sec
print("turning on php services....")
for pause_in_secound in [3]:
    time.sleep(pause_in_secound)
#sleep fun 2 sec



data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                    'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))