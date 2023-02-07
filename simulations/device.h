#ifndef __DEVICE_H__
#define __DEVICE_H__

#include <line.h>
#include <list>

enum DeviceState {
    normal = 0,
    sending = 1,
    recieving = 2,
};

class Device {
    public:
        // constructor/destructors
        Device(int id);
        Device(int id, Line* line);

        // device default property interfaces
        int getID(){ return device_id; }

        void sendData();
        void recieveData();
        DeviceState getState();

        // line properties
        void removeLine(Line* line);
        void addLine(Line* line);

        // data properties
        void addData(void* data);

    private:
        int device_id;
        void* data;
        DeviceState state;

        std::list<Line*> lines;
        
};

#endif