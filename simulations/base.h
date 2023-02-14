#ifndef __BASE_H__
#define __BASE_H__

#include <iostream>

#include "data.h"

class Base {
    public:
        Base(){}
        Base(int id){ Base::id = id; }

        virtual void recieve(Data* data) { Base::data = data; }

        virtual void setID(int id) { Base::id = id; }
        virtual int getID() { return id; }
        virtual Data* getData() { return data; }
        
        virtual void removeData() { data = 0; }
        virtual friend std::ostream& operator<<(std::ostream& os, const Base& base);

    private:
        Data* data;
        int id;

};

std::ostream& operator<<(std::ostream& os, const Base& base) {
    os << *base.data;
    return os;
}

#endif