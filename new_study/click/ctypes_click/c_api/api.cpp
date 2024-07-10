#include "./api.h"
#include <iostream>
#include <vector>

using namespace std;

#ifdef __cplusplus
extern "C" {
#endif

void create(uint32_t id, test1_t t1, test2_t t2)
{
    cout << "t1.a" << t1.a << endl;
    cout << "t1.b" << t1.b << endl;
    vector<uint32_t> v1(t2.list, t2.list+t2.cnt);
    for (auto i : v1) {
        cout << "val: " << i << endl;
    }
}

#ifdef __cplusplus
}
#endif
