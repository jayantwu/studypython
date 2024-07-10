
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    uint32_t a;
    uint64_t b;
} test1_t;

typedef struct {
    uint32_t cnt;
    uint32_t *list;
}test2_t;

void create(uint32_t id, test1_t t1, test2_t t2);


#ifdef __cplusplus
}
#endif


