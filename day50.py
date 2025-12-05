import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bytes_to_mb(value):
    return value / (1024 * 1024)

def monitor_system():
    old_net = psutil.net_io_counters()
    
    while True:
        clear_screen()
        
        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)

        # RAM
        ram = psutil.virtual_memory()
        ram_used = bytes_to_mb(ram.used)
        ram_total = bytes_to_mb(ram.total)

        # Disk
        disk = psutil.disk_usage('/')
        disk_used = bytes_to_mb(disk.used)
        disk_total = bytes_to_mb(disk.total)

        # Network
        new_net = psutil.net_io_counters()
        upload_speed = (new_net.bytes_sent - old_net.bytes_sent) / 1024
        download_speed = (new_net.bytes_recv - old_net.bytes_recv) / 1024
        old_net = new_net

        print("===============================================")
        print("           SYSTEM RESOURCE MONITOR")
        print("===============================================\n")

        print(f"CPU Usage        : {cpu_usage}%")
        print(f"RAM Usage        : {ram_used:.2f} MB / {ram_total:.2f} MB")
        print(f"Disk Usage       : {disk_used:.2f} MB / {disk_total:.2f} MB")

        print(f"Upload Speed     : {upload_speed:.2f} KB/s")
        print(f"Download Speed   : {download_speed:.2f} KB/s")

        print("\nRefreshes every 1 second... (Press CTRL + C to stop)")

        time.sleep(1)

if __name__ == "__main__":
    monitor_system()
