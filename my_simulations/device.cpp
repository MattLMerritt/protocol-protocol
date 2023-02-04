#include <device.h>

Device::Device(int id){
    Device::device_id = id;   
}

void Device::removeLine(Line* line) {
    //Device::line = 0;
}

void Device::addLine(Line* line) {
    //Device::line = line;
}

void Device::addData(void* data){
    Device::data = data;
}

/*================== my implementation ================*/

void Device::setAddress(int address) {
    Device::device_address = address;
}


