#ifndef __TIMER_H__
#define __TIMER_H__

class Timer {
    public:
        Timer();
        void setTimerId(unsigned int new_timer_id);
        void setClockRate(unsigned int new_clock_rate);

    private:
        unsigned int timer_id;
        unsigned int clock_rate;
        unsigned int current_ticks;
};

#endif