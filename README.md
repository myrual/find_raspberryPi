find_raspberryPi
================

find local network raspberry pi by UDP command. Make sure RPI and PC/MAC in same network before follow the instruction.

##HOW TO 
###on Rapsberry pi:

#####Clone code

```
git clone git@github.com:myrual/find_raspberryPi.git
```

#####update script
enter the code directory and update startup by change the file directory of udp_startup.py to current path

#####add startup script to debian 

```
sudo cp startup /etc/init.d
sudo chmod 755 /etc/init.d/startup
sudo chown root:root /etc/init.d/startup

sudo update-rc.d startup defaults
```

#####reboot raspberry pi 


###on pc/mac
```
python udp_find_hello.py 
```
The code will show the ip which RPI using.

