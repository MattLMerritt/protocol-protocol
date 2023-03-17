#ifndef __LINE_H__
#define __LINE_H__

#include "base.h"

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

        void connectIncomingConnection(Base* inc){ incoming = inc; }
        void connectOutgoingConnection(Base* out){ outgoing = out; }
    private:
        Base* incoming;
        Base* outgoing;

};

inline std::ostream& operator<<(std::ostream& os, const Line& line) {
    os << "Line " << line.getID() << ": " << *(line.getData());
    return os;
}

#endif