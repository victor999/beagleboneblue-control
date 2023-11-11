# beagleboneblue-control
Hardware control using beaglebone blue

# Installation

Download the latest console image from https://rcn-ee.net/rootfs/bb.org/testing/

The name should contain bone...debian...console-armhf

Flash image onto SD card.

Boot BBBlue fromSD card.

Connect to BBBlue via the COM port (115200 baudrate) or ssh to USB network (192.168.7.2)

Grow partition to fill all available space:
```
sudo /opt/scripts/tools/grow_partition.sh
```

Reboot

Connect to the internet

```
# connmanctl
# connmanctl> scan wifi
# connmanctl> services
# connmanctl> agent on
# connmanctl> connect wifi_****
Enter passphrase
# connmanctl> quit
```

I am using Adafruit BBIO python library and librobotcontrol

The configuration that I found working with this stuff is ti-rt kernel 4.19 (default kernel from the image)

You can update your kernel:
```
sudo /opt/scripts/tools/update_kernel.sh --ti-rt-kernel --lts-4_19
```

Adafruit BBIO install:

https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu

librobotcontrol installation:
```
sudo apt install librobotcontrol
```

I didn't succeed to run motors 1 and 2 by Adafruit because of some GPIO conflicts, I need to figure it out.

librobotcontrol runs everything just fine

# Tests

BBIO:
```
sudo python Adafruit_bbio/test.py
```
Librobotcontrol:
```
sudo rc_test_motors -m 3 -d 0.5
sudo rc_test_servos -c 1 -s 1.4 0.0
```

