#ifndef __LINE_H__
#define __LINE_H__

#include <device.h>

class Line : public virtual Base {
    public:
        // constructor/destructors
        Line();

        // line default property interfaces
        void transmit();
        void recieve(void* data);
        void getQueue(); // not concrete yet

        // line properties
        void removeLine();
        void removeIncomingConnection();
        void removeOutgoingConnection();

        void connectIncomingDevice(Device inc){ incoming = &inc; }
        void connectOutgoingDevice(Device out){ outgoing = &out; }
        void connectIncomingLine(Line inc){ incoming = &inc; }
        void connectOutgoingLine(Line out){ outgoing = &out; }
        
        void printInformation();

    private:
        void* incoming;
        void* outgoing;

        void* data;
};

#endif