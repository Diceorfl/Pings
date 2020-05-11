# Pings  
## Аdvanced analog of the ping system utility/Усовершенствованный аналог системной утилиты ping  

### Как это работает?  
    Скрипт передаёт с указанным периодом запросы по заданному IP адресу и принимет ответы.  
    Каждый переданный запрос отображается со штампом времени в таком виде: 123.456 192.168.1.1 Send to 192.168.2.1 bytes=32   
    Каждый принятый ответ отображается вместе с разницей от запроса до ответа в таком виде: 123.789 192.168.1.1 Get from 192.168.2.1 bytes=32 dtime=123  
### Управление:  
    Ключи:    
      /? - Вывод хелпа (любой неизвестный ключ)  
      /n=count - число повторов (если не задано, то 4)  
      /l=size - размер пакета в байтах (по умолчанию 32)  
      /w=timeout - таймаут в мс для ожидания ответа (по умолчанию 1000)  
      /t=time - период передачи в мс (по умолчанию 1000)  

### Description  
    The script transmits requests with the specified period to the specified IP address and receives responses.  
    Each transmitted request is displayed with a time stamp in the following form: 123.456 192.168.1.1 Send to 192.168.2.1 bytes = 32  
    Each accepted answer is displayed together with the difference from the request to the answer in the following form:  
    123.789 192.168.1.1 Get from 192.168.2.1 bytes = 32 dtime = 123    
### How does it work?  
    Keys:  
      /? - Help output (any unknown key)  
      /n=count - number of retries (default is 4)  
      /l=size - packet size in bytes (default is 32)  
      /w=timeout - timeout in ms to wait for a response (default is 1000)  
      /t=time - transmission period in ms (default is 1000)  
