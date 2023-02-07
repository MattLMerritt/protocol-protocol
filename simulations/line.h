#ifndef __LINE_H__
#define __LINE_H__

#include <device.h>

class Line {
    public:
        // constructor/destructors
        Line();
        Line(void* incoming, void* outgoing);

        // line default property interfaces
        void transmit();
        void recieve();
        void getQueue(); // not concrete yet

        // line properties
        void removeLine();
        void removeIncomingConnection();
        void removeOutgoingConnection();

        void addIncomingConnection(void* inc);
        void addOutgoingConnection(void* out);

        void addData(void* data);
        
        void printInformation();

    private:
        void* incoming;
        void* outgoing;

        void* data;
};

#endif