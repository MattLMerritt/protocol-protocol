#ifndef __DEVICE_H__
#define __DEVICE_H__

#include <line.h>
#include "base.h"
#include <list>

enum DeviceState {
    normal = 0,
    sending = 1,
    recieving = 2,
};

class Device : public virtual Base {
    public:
        // constructor/destructors
        Device(int id);
        Device(int id, Line* line);

        void sendData();
        DeviceState getState(){ return state; }

        // line properties
        void removeLine(Line* line);
        void addLine(Line* line);

    private:
        DeviceState state;
        std::list<Line*> lines;
        
};

#endif