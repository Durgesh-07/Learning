#include<stdio.h>
int main(){
    int n;
    FILE *fd1,*fd2;
    fd1 = fopen("input.txt","r");
    fd2 = fopen("output.txt","w");
    fscanf(fd1,"%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        fscanf(fd1,"%d",&arr[i]);
    }
    fclose(fd1);
    for(int i=0;i<n;i++){
        fprintf(fd2,"%d ",arr[i]);
    }
    fflush(fd2);
    fclose(fd2);
    return 0;
}