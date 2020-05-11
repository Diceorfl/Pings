import socket
import sys
import time
from threading import Thread

def run(host,port,l,w,start):
  try: #Попытка соединиея с указаным адресом, иначе сообщение об ошибке и выход
    s = socket.create_connection((host,port))
  except socket.error as error:
    print(error)
    sys.exit(1)
  s.settimeout(w/1000)
  try: #Попытка отправки и получения сообщения
    getsize = len("GET /text HTTP/2.0\r\n\r\n".encode())
    s.send("GET /text HTTP/2.0\r\n\r\n".encode()+bytearray([1]*(l-getsize)))
    now = time.time()
    print ("%.4f"%(now-start),socket.gethostbyname(socket.gethostname()), \
           " Send to  ",socket.gethostbyname(host),"bytes =",l)
    lendata = 0
    while lendata < l:
      try: #Попытка получить данные
        data = s.recvfrom(l-lendata)
      except:
        print("Check your settings. May be too much data to send!")
        sys.exit(1)
      lendata += len(data)
    dtime = time.time() - now
    print ("%.4f"%(dtime+now-start),socket.gethostbyname(socket.gethostname()),\
    " Get from ", socket.gethostbyname(host), "bytes =",lendata, "dtime =","%.4f"%(dtime),"sec")
  except socket.timeout as error:
    print(error)
  s.close()

#проврекрка аргументов в командной строке и вывод хелпа
keys = ["/?","/n","/l","/w","/t"]
help = "Help: Ping.py ya.ru /n=number of repetitions    /l=bytes    /w=response timeout    /t=period of send"
if len(sys.argv) < 2 or "/?" in sys.argv:
    print(help)
    sys.exit(1)
host = sys.argv[len(sys.argv)-1]
if "/" in host:
    print(help)
    sys.exit(1)
sys.argv.remove(host)
n = 4 #число повторов
l = 32 #размер получаемого пакета
w = 1000 #таймаут в мс для ожидания ответа
t = 1000 #период передачи в мс
if len(sys.argv) >= 2:
  for i in range(1,len(sys.argv)):
    if sys.argv[i][0:2] in keys:
        key = sys.argv[i][0:2]
        if key == keys[1]: n = int(sys.argv[i][3:])
        if key == keys[2]: l = int(sys.argv[i][3:])
        if key == keys[3]: w = float(sys.argv[i][3:])
        if key == keys[4]: t = float(sys.argv[i][3:])
    else:
        print(help)
        sys.exit(1)
start = time.time()
threadlist = []
for i in range(0,n):
  thread = Thread(target=run, args=(host,80,l,w,start))
  thread.start()
  threadlist.append(thread)
  time.sleep(t/1000)
for i in range(0,n):
  threadlist[i].join()
