#ifndef __TIMER_H__
#define __TIMER_H__

#include <stdint.h>

/* TIMER

currently the timer just tracks the ticks 
(basically at every frame of a scene it will tick up and count like a frame)

TO BE IMPLEMENTED:
- have it represent seconds (fps) -> get OS to track that maybe using another API?

*/

class Timer {
    public:
        Timer();
        Timer(int64_t begin_ticks);

    private:
        int64_t current_ticks;
        //double us_per_tick;
        //double ms_per_tick;

};

#endif