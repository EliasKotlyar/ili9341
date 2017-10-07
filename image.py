# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from PIL import Image
import A20_GPIO as GPIO
import ILI9341 as TFT

# default PINs, BCM GPIO
pin_RST = GPIO.UEXT1_3 # White
pin_DC = GPIO.UEXT1_4 # Grey
pin_LED = GPIO.UEXT1_5 # Green
pin_MISO = GPIO.UEXT1_6 # Yellow
pin_MOSI = GPIO.UEXT1_7 # Purple
pin_CLK = GPIO.UEXT1_8 # Blue
pin_CS = GPIO.UEXT1_9 # Brown





# Create TFT LCD display class.
disp = TFT.ILI9341(pin_RST,pin_DC,pin_LED,pin_MISO,pin_MOSI,pin_CLK,pin_CS)

# Initialize display.
disp.begin()

# Load an image.
print 'Loading image...'
image = Image.open('cat.jpg')

# Resize the image and rotate it so it's 240x320 pixels.
image = image.rotate(90).resize((240, 320))

# Draw the image on the display hardware.
print 'Drawing image'
disp.display(image)
