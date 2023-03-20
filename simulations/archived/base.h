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

        virtual int getID() const { return id; }
        virtual Data* getData() const { return data; }
        
        virtual void removeData() { data = 0; }

    private:
        Data* data;
        int id;

};

inline std::ostream& operator<<(std::ostream& os, const Base& base) {
    os << base.getData();
    return os;
}

#endif