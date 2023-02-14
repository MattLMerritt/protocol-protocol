#include <line.h>
#include <iostream>

Line::Line(int id){
    Line::incoming = 0;
    Line::outgoing = 0;
    setID(id);
}

void Line::transmit(){
    outgoing->recieve(outgoing->getData());
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

void Line::printInformation() {
    //std::cout << "Incoming Device ID: " + Line::incoming_device->getID() << std::endl;
    //std::cout << "Outgoing Device ID: " + Line::outgoing_device->getID() << std::endl;
    //if(data != 0){
    //    std::cout << data << std::endl;
    //}
}