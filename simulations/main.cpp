#include <stdio.h>
#include <stdlib.h>

#include <device.h>
#include <line.h>
#include <globalqueue.h>
#include <event.h>

#include <testdata.h>

#include <timer.h>

int main(){

    // Initialize a global queue
    GlobalQueue global;

    // Add test data
    TestData data1("josh", 2, 14);
    TestData data2("brian", 3, 2);

    // Initialize Devices
    Device device_one(1);
    Device device_two(2);

    // Add wires/lines    
    //Line line_one() ;

    std::cout << data1 << std::endl;
    std::cout << data2 << std::endl;

    return 0;
}