#include <line.h>

Line::Line(){
    Line::incoming_device = 0;
    Line::outgoing_device = 0;
}

Line::Line(Device* incoming, Device* outgoing) {
    Line::addIncomingConnection(incoming);
    Line::addOutgoingConnection(outgoing);
}

// removes the line from a devices
void Line::removeLine(){
    Line::removeIncomingConnection();
    Line::removeOutgoingConnection();
}

void Line::removeIncomingConnection(){
    if(Line::incoming_device != 0){
        Line::incoming_device->removeLine();
        Line::incoming_device = 0;
    }
}

void Line::removeOutgoingConnection(){
    if(Line::outgoing_device != 0){
        Line::outgoing_device->removeLine();
        Line::outgoing_device = 0;
    }
}

// add the line to the device
void Line::addIncomingConnection(Device* device){
    if(Line::incoming_device == 0){
        Line::incoming_device = device;
    }
}

void Line::addOutgoingConnection(Device* device){
    if(Line::outgoing_device == 0){
        Line::outgoing_device = device;
    }
}