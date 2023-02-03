#include <device.h>

Device::Device(int id){
    Device::device_id = id;   
}

void Device::removeLine(Line* line) {
    Device::lines.remove(line);
}

void Device::addLine(Line* line) {
    Device::lines.insert(lines.begin(), line);
}

void Device::addData(void* data){
    Device::data = data;
}
