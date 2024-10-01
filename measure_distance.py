import RPi.GPIO as GPIO        # Import GPIO library
import time                    # Import time library
from openpyxl import Workbook   # Import Workbook for Excel

# Set GPIO pin numbering 
GPIO.setmode(GPIO.BCM)

TRIG = 15  # Associate pin 15 to TRIG
ECHO = 14  # Associate pin 14 to ECHO

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
GPIO.setup(ECHO, GPIO.IN)   # Set pin as GPIO in

# Create an Excel workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "Distance Measurements"
ws.append(["Timestamp", "Distance (cm)"])  # Header row

while True:
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    print("Waiting For Sensor To Settle")
    time.sleep(2)  # Delay of 2 seconds

    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW

    while GPIO.input(ECHO) == 0:  # Check if Echo is LOW
        pulse_start = time.time()  # Time of the last LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether Echo is HIGH
        pulse_end = time.time()  # Time of the last HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Pulse duration

    distance = pulse_duration * 17150  # Calculate distance
    distance = round(distance, 2)  # Round to two decimal points

    if distance > 20 and distance < 400:  # Is distance within range
        final_distance = distance - 0.5  # Calibrate the distance
        print(f"Distance: {final_distance} cm")
        
        # Record the data to Excel
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        ws.append([timestamp, final_distance])
        
        # Save the Excel file after each reading
        wb.save("distance_measurements.xlsx")
    else:
        print("Out Of Range")  # Display out of range
