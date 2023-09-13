import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

# config for matrix
options = RGBMatrixOptions()
# configure for display settings, Script is set to 64x64 but can be overriden using --led-rows and --led-cols flags
options.rows = 64
options.cols = 64
# mapping used for GPIO pins for RPI, if using Hat or Bonnet set options from documentation
options.hardware_mapping = 'regular'
# Set max refresh rate
options.show_refresh_rate = True
options.limit_refresh_rate_hz = 60
options.brightness = 50
# This config is used for troubleshooting with the audio driver in the RPI.
options.disable_hardware_pulsing = True
options.scan_mode = 1
# use this option to higher power devices 0-6, 3 is good for RPI 3 and 4
options.gpio_slowdown = 3
# Apply config to Libarary
matrix = RGBMatrix(options = options)

# Open image, resize and convert to RGB for Display.
image = Image.open('rancher_prime.jpg')
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# Display Image on Matrix
matrix.SetImage(image.convert('RGB'))

# used to quit script
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)