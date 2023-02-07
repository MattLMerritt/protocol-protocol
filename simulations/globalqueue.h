#ifndef __GLOBAL_QUEUE_H__
#define __GLOBAL_QUEUE_H__

#include <stdint.h>
#include <event.h>
#include <queue>

class GlobalQueue {
    public:
        GlobalQueue();

        // global queue functionality
        void addEvent(uint32_t time, Event event);
        void processNext();

    private:
        std::queue<Event> events;    // will change later as soon as we deal with bigger data
};

#endif