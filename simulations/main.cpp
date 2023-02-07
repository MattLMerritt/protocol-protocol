#include <stdio.h>
#include <stdlib.h>



#include <device.h>
#include <line.h>
#include <globalqueue.h>
#include <event.h>

#include <timer.h>

int main(){

    // Initialize a global queue
    GlobalQueue global;

    // Initialize Devices
    Device device_one(1);
    Device device_two(2);

    // Add wires/lines    
    Line message(&device_one, &device_two);
    Line rec(&device_two, &device_one);

    

    return 0;
}