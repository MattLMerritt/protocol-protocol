#ifndef __DATA_H__
#define __DATA_H__

#include <iostream>

class Data { 
    public:
        virtual friend std::ostream& operator<<(std::ostream& os, const Data& data);
};

#endif