#ifndef __LINE_H__
#define __LINE_H__

#include <device.h>
#include <data.h>
#include <base.h>

class Line : public virtual Base {
    public:
        // constructor/destructors
        Line(int id);

        // line default property interfaces
        void transmit();
        // void recieve(Data* data);
        void getQueue(); // not concrete yet

        // line properties
        void removeLine();
        void removeIncomingConnection();
        void removeOutgoingConnection();

        void connectIncomingDevice(Device inc){ incoming = &inc; }
        void connectOutgoingDevice(Device out){ outgoing = &out; }
        void connectIncomingLine(Line inc){ incoming = &inc; }
        void connectOutgoingLine(Line out){ outgoing = &out; }

    private:
        Base* incoming;
        Base* outgoing;

};

#endif