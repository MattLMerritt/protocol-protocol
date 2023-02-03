#include <device.h>

Device::Device(int id){
    Device::device_id = id;   
}

void Device::removeLine() {
    Device::line = 0;
}

void Device::addLine(Line* line) {
    Device::line = line;
}