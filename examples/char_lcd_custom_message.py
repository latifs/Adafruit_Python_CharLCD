#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import Adafruit_CharLCD as LCD
import sys

# Raspberry Pi pin configuration:
lcd_rs = 26  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 06
lcd_d6 = 05
lcd_d7 = 11
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# retrieves the message
text_to_display1 = sys.argv[1]
text_to_display2 = sys.argv[2]

# Print a two line message
lcd.message(text_to_display1 + '\n' + text_to_display2)
