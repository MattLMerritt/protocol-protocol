#include <device.h>

Device::Device(int id){
    setID(id);
}

void Device::removeLine(Line* line) {
    Device::lines.remove(line);
}

void Device::addLine(Line* line) {
    Device::lines.insert(lines.begin(), line);
}

void Device::sendData() {
    for(Line* line : lines){
        line->recieve(getData());
    }
    removeData();
}
