#ifndef __GLOBAL_QUEUE_H__
#define __GLOBAL_QUEUE_H__

#include <stdint.h>
#include <event.h>

class GlobalQueue {
    public:
        GlobalQueue();

        // global queue functionality
        void addEvent(uint32_t time, Event event);
        void processNext();

    private:

};

#endif