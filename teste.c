#include <stdio.h>
#include <time.h>

int main(void) {
    time_t t = time(NULL);
    
    double vec[3] = {0.0, 0.0, 0.0};
    for (long long i = 0; i < 10000000; i++) {
        vec[0] += 0.1;
        vec[1] += 0.1;
        vec[2] += 0.1;
    }
    
    printf("Tempo: %f\n", (double)(time(NULL) - t));
    return 0;
}