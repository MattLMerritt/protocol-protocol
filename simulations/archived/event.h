#ifndef __EVENT_H__
#define __EVENT_H__

#include <string>

class Event {
    public:
        Event() {};

        virtual void triggerEvent();

    private:
        std::string temporary; // remove this if we figure out what event should be
};

#endif