#include <stdio.h>
#include <stdlib.h>


#include <scene.h>
#include <frame.h>

#include <device.h>
#include <line.h>

#include <timer.h>

int main(){

    // Intialize Devices
    Device device_one(1);
    Device device_two(2);

    // Add wires/lines    
    Line message(&device_one, &device_two);
    Line rec(&device_two, &device_one);

    

    return 0;
}