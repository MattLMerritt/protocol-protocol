#include "device.h"

Device::Device(int id){
    setID(id);
}

void Device::removeIncomingLine(Line* line) {
    Device::incomingLines.remove(line);
}

void Device::removeOutgoingLine(Line* line) {
    Device::outgoingLines.remove(line);
}

void Device::addIncomingLine(Line* line) {
    Device::incomingLines.insert(incomingLines.begin(), line);
}

void Device::addOutgoingLine(Line* line) {
    Device::outgoingLines.insert(outgoingLines.begin(), line);
}

void Device::sendData() {
    for(Line* line : outgoingLines){
        line->recieve(getData());
    }
    removeData();
}

void Device::recieve(Data* data) {
    for(Line* line : incomingLines){
        // override previous data entries when there are 
        // multiple data flowing into one line
        data = line->getData();
    }
}
