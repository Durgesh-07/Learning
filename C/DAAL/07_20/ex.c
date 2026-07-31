#include<stdio.h>
int main(int argc,char* argv[]){
    FILE *fd;
    int arr[5],n,i;
    n = atoi(argv[1]);
    fd = fopen(argv[2],"r");
    for(i=0;i<n;i++){
        fscanf(fd,"%d",&arr[i]);
        printf("%d",arr[i]);
    }
    fclose(fd);
    return 0; // ./a.out 5 input.txt
}