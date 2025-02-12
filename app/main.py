from flask import Flask, render_template
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
        'disk_count': len(disk_info)
    }
    
    system_information = {
        'platform': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'system_uptime': int((time.time() - psutil.boot_time()) / 60),
        'system_uptime_hours': int((time.time() - psutil.boot_time()) / 3600)
    }
    
    return render_template('index.html', 
                         system_health=system_health,
                         system_information=system_information)

@app.route('/collection')
def collection():
    return 'Collection!'

@app.route('/collection/<int:collection_id>')
def collection_id(collection_id):
    return 'Collection ID: {}'.format(collection_id)

@app.route('/collection/<int:collection_id>/item')
def collection_item(collection_id):
    return 'Collection Item!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
