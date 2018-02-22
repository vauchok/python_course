""" This is python app which are monitoring the system/server"""
import json
import time
import psutil
import settings


def collect_data():
    """Return the dictionary which consist of monitoring information"""
    disk = psutil.disk_io_counters(perdisk=False)
    net = psutil.net_io_counters()
    output_data = {
        'Overall CPU load': psutil.cpu_percent(interval=1),
        'Overall memory usage': psutil.virtual_memory().percent,
        'Overall virtual memory usage': psutil.swap_memory().percent,
        'IO information': {
            'number of reads': disk.read_count,
            'number of writes': disk.write_count,
            'number of bytes read': disk.read_bytes,
            'number of bytes written': disk.write_bytes,
            'time spent reading from disk': disk.read_time,
            'time spent writing to disk': disk.write_time,
            'time spent doing actual I/Os': disk.busy_time,
        },
        'Network information': {
            'number of bytes sent': net.bytes_sent,
            'number of bytes received': net.bytes_recv,
            'number of packets sent': net.packets_sent,
            'number of packets received': net.packets_recv,
        }
    }
    settings.snapshot_number += 1
    return {'SNAPSHOT ' + str(settings.snapshot_number) + ':' +
            str(time.asctime()): output_data}


def monitoring(output):
    """Create/write monitoring information to log.file"""
    with open('data.'+output, 'a') as outfile:
        outfile.write(json.dumps(collect_data()) + '\n')
        outfile.close()


while True:
    try:
        monitoring(settings.output)
        time.sleep(settings.interval * 60)
    except KeyboardInterrupt as error:
        print(error)
break
