#ifndef __TEST_DATA_H__
#define __TEST_DATA_H__

#include <stdlib.h>
#include <string>

#include "data.h"

class TestData : public virtual Data {
    public:
        TestData(std::string n, int m, int d) {
            name = n;
            month = m;
            day = d;
        }

        friend std::ostream& operator<<(std::ostream& os, const TestData& td);
    private:
        std::string name;
        int month;
        int day;
};

std::ostream& operator<<(std::ostream& os, const TestData& td){
    os << "Today is: " << td.month << '/' << td.day << "\nHappy Birthday " << td.name << '!' << std::endl;
    return os;
}

#endif