from flask import Flask, request, render_template

import os
import psutil
import platform 
import time

app = Flask(__name__)

@app.route('/') 
def index(): 
    # Get all disk partitions and their usage
    disk_info = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'total': f"{usage.total / (1024**3):.2f} GB",
                'used': f"{usage.used / (1024**3):.2f} GB",
                'free': f"{usage.free / (1024**3):.2f} GB",
                'percent': usage.percent
            })
        except:
            continue

    system_health = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_info': disk_info,
        'disk_count': len(disk_info),
        'boot_time': psutil.boot_time()
    }
    
    system_information = {
        'platform': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'system_version': platform.version(),
        'python_version': platform.python_version(),
        'system_uptime': int((time.time() - psutil.boot_time()) / 60), 
        'system_uptime_hours': int((time.time() - psutil.boot_time()) / 3600)
    }
    
    return render_template('index.html', 
                         system_health=system_health,
                         system_information=system_information)
 
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/cpu')
def cpu():
    return render_template('cpu.html')

@app.route('/memory')
def memory():
    return render_template('memory.html')

@app.route('/disk')
def disk():
    return render_template('disk.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/get_cpu')
def get_cpu():
    cpu = psutil.cpu_percent(interval=1)
    return str(cpu)

if __name__ == '__main__':
    app.run(debug=True)
