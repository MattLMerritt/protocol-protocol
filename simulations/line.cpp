#include <line.h>
#include <iostream>

Line::Line(){
    Line::incoming = 0;
    Line::outgoing = 0;
}

Line::Line(void* incoming, void* outgoing) {
    Line::addIncomingConnection(incoming);
    Line::addOutgoingConnection(outgoing);
}

// removes the line from a devices
void Line::removeLine(){
    Line::removeIncomingConnection();
    Line::removeOutgoingConnection();
}

/*
void Line::removeIncomingConnection(){
    if(Line::incoming != 0 && (&Line::incoming)){
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
*/

// add the line to the device
/*
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
*/
void Line::addData(void* data){
    Line::data = data;
}

void Line::printInformation() {
    //std::cout << "Incoming Device ID: " + Line::incoming_device->getID() << std::endl;
    //std::cout << "Outgoing Device ID: " + Line::outgoing_device->getID() << std::endl;
    //if(data != 0){
    //    std::cout << data << std::endl;
    //}
}