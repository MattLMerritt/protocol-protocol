#ifndef __LINE_H__
#define __LINE_H__

#include <device.h>

class Line {
    public:
        Line();
        Line(void* incoming, void* outgoing);


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