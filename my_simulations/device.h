#ifndef __DEVICE_H__
#define __DEVICE_H__

#include <line.h>

class Device {
    public:
        Device(int id);
        Device(int id, Line* line);

        void removeLine(Line* line);
        void addLine(Line* line);
        void addData(void* data);

        void sendData();

        int getID(){ return device_id; }

    private:
        int device_id;
        Line** lines;

        void* data;
};

#endif