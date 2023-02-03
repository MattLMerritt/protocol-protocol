#ifndef __DEVICE_H__
#define __DEVICE_H__

#include <line.h>

class Device {
    public:
        Device(int id);
        Device(int id, Line* line);

        void removeLine();
        void addLine(Line* line);

        int getID(){ return device_id; }

    private:
        int device_id;
        Line* line;
};

#endif