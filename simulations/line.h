#ifndef __LINE_H__
#define __LINE_H__

#include <device.h>

class Line {
    public:
        Line();
        Line(Device* incoming, Device* outgoing);


        void removeLine();
        void removeIncomingConnection();
        void removeOutgoingConnection();

        void addIncomingConnection(Device* device);
        void addOutgoingConnection(Device* device);

        
        void printInformation();

    private:
        Device* incoming_device;
        Device* outgoing_device;

        void* data;
};

#endif