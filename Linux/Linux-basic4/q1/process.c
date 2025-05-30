#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>

int main(){
    int pid;
    int status;
    int terminatedPid;
    if((pid=fork()) == 0){
        // printf("makeprocess.out is unnecessary process. please kill this one\n");
        sleep(500);
    }
}