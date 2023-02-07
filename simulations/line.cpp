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
    removeIncomingConnection();
    removeOutgoingConnection();
}

void Line::removeIncomingConnection(){
    Line::incoming = 0;
}

void Line::removeOutgoingConnection(){
    Line::outgoing = 0;
}

// add the line to the device
void Line::addIncomingConnection(void* inc){
    if(Line::incoming_device == 0){
        Line::incoming_device = device;
    }
}

void Line::addOutgoingConnection(void* out){
    if(Line::outgoing_device == 0){
        Line::outgoing_device = device;
    }
}

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