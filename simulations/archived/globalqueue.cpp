#include "globalqueue.h"

GlobalQueue::GlobalQueue() {
    // TO BE IMPLEMENTED
}

void GlobalQueue::addEvent(uint32_t time, Event event) {
    // TO BE IMPLEMENTED (TIME)
    events.push(event);
}

void GlobalQueue::processNext() {
    while(!events.empty()){
        events.front().triggerEvent();
        events.pop();
    }
}