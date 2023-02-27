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

        std::string getName() const { return name; }
        int getMonth() const { return month; }
        int getDay() const { return day; }

    private:
        std::string name;
        int month;
        int day;
};

std::ostream& operator<<(std::ostream& os, const TestData& td){
    os << "Today is: " << td.getMonth() << '/' << td.getDay() << "\nHappy Birthday " << td.getName() << '!' << std::endl;
    return os;
}

#endif