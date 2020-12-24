import time
import board
import adafruit_dht
from Adafruit_IO import Client, Feed, RequestError

# Global Variables
AIO_USERNAME    = ""
AIO_KEY         = ""
AIO_TEMP_FEED = "temp"
AIO_HUM_FEED = "hum"


#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D13) # depende de donde este conectado el sensor

# Adafruit IO configuration
aio = Client(AIO_USERNAME, AIO_KEY)  # create Adafruit IO REST client instance
hum_feed = aio.feeds(AIO_HUM_FEED)
temp_feed = aio.feeds(AIO_TEMP_FEED)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C   Humidity: {}% ".format(temperature_c, humidity))
        aio.send(temp_feed.key, temperature_c)
        time.sleep(2)
        aio.send(hum_feed.key, humidity)
    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    time.sleep(2)
