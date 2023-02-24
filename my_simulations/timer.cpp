#include <timer.h>

// ===============================================================
//                          Constructors
// ===============================================================

Timer::Timer(){
    this.timer_id = 0; // default timer id
    this.clock_rate = 1e9; // default clock rate
    this.current_ticks = 0;
}

void Timer::setTimerId(unsigned int new_timer_id) {
    this.timer_id = new_timer_id;
}

void Timer::setClockRate(unsigned int new_clock_rate) {
    this.clock_rate = new_clock_rate;
}
