#ifndef __DATA_H__
#define __DATA_H__

#include <iostream>

class Data { };

inline std::ostream& operator<<(std::ostream& os, const Data& data){ return os; }

#endif