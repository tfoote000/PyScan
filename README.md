# PyScan

This is a really simple project that I have put together.

I purchased a 433MHz barcode scanner on Prime Day [Link Here](https://smile.amazon.com/gp/product/B01GDJ2BH6). I wanted to use this scanner to be able to scan barcodes into my [Home Assistant](https://www.home-assistant.io/) or [Node Red](https://nodered.org/).

This script creates a docker container that listens for the Serial response from the USB dongle in this particular scanner. It then will send a webhook (POST Method) to the provided environment variable.

# Usage
```
docker pull tfoote000/pyscan
docker run --device <host path>:<contianer path> -e COM_PORT=<container device path> -e WEBHOOK_URL=<webhook url> tfoote000/pyscan
```
