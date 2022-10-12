''' Stream magnetometer data to serial port.
Matthew Oppenheim
v0.0 July 2021 '''

from microbit import *
import utime

# Measurement window in ms. Mains is 50Hz, which gives 20 ms as minimum.
WINDOW = 1000
# How much time in ms between samples
INTERVAL = 13

def calibrate_compass():
    ''' Calibrate the compass if necessary. '''
    if not compass.is_calibrated():
        compass.calibrate()

def arr_avg(arr):
    ''' Get average value of an array.
    >>> arr_avg([1,2,3,4])
    2
    '''
    return int(sum(arr)/len(arr))

def arr_max(arr):
    ''' Get highest value in an array. '''
    return max(arr)


def arr_delta(arr):
    ''' Get max-min for an array. '''
    return max(arr) - min(arr)


def start_screen():
    ''' Display pattern.'''
    print("starting stream_magnetometer")
    display.show(Image.TARGET)


def main():
    start_screen()
    # calibrate_compass()
    while True:
        deadline = utime.ticks_add(utime.ticks_ms(), WINDOW)
        mag_x_arr = []
        mag_y_arr = []
        mag_z_arr = []
        mag_total_arr = []
        while utime.ticks_diff(deadline, utime.ticks_ms()) > 0:
            mag_x = compass.get_x()
            mag_y = compass.get_y()
            mag_z = compass.get_z()
            #mag_total = compass.get_field_strength()
            mag_x_arr.append(mag_x)
            mag_y_arr.append(mag_y)
            mag_z_arr.append(mag_z)
            sleep(INTERVAL)
        mag_x_delta = arr_delta(mag_x_arr)
        mag_y_delta = arr_delta(mag_y_arr)
        mag_z_delta = arr_delta(mag_z_arr)
        print("({},{},{})".format(mag_x_delta, mag_y_delta, mag_z_delta))

main()
