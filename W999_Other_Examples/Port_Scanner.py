""" Port Scanner
"""
import queue
import threading
import socket

import paramiko

MY_IP = socket.gethostbyname(socket.gethostname())
IP_RANGE = [".".join([*MY_IP.split(".")[:3], str(i)]) for i in range(1, 255)]
# IP_RANGE = [f"192.168.0.{i}" for i in range(1, 255)]

print(f"IP SCAN RANGE: {IP_RANGE[0]}-{IP_RANGE[-1]}")

USERNAME = "nstech"
PASSWORD = "25637238"
COMMEND = ""

socket.setdefaulttimeout(5)
PRINT_LOCK = threading.Lock()
QUE = queue.Queue()

def queue_push(addr: str):
    # print(f"\rscanning... {addr}", end="")
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((addr, 22))
        con.send(b'Primal Security \n')
        service_name = con.recv(1024)
        host_name = socket.getfqdn(addr)
        print(service_name, host_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(addr, port=22, username=USERNAME, password=PASSWORD)
        stdin, stdout, stderr = ssh.exec_command("hostname")
        lines = stdout.readlines()
        with PRINT_LOCK:
            print(f"{lines[0].strip()} :")
            print(f"ssh {USERNAME}@{addr} {COMMEND}")
            # print(f"{addr}() Open: {service_name.decode('utf-8').strip()}")
        con.close()
        ssh.close()
    except socket.error as e:
        pass
    except paramiko.AuthenticationException as e:
        pass
    return

def queue_get():
    while True:
        worker = QUE.get()
        queue_push(worker)
        QUE.task_done()
    return

if __name__ == '__main__':
    for i in range(30):
        thread_push = threading.Thread(target=queue_get)
        thread_push.daemon = True
        thread_push.start()
    for _addr in IP_RANGE:
        QUE.put(_addr)
    QUE.join()
