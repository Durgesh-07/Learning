#include<stdio.h>
int main(){
    int arr[10],i,n;
    FILE *fd1,*fd2;
    fd1 = fopen("input.txt","r");
    fd2 = fopen("output.txt","w");
    fscanf(fd1,"%d",&n);
    for(i=0;i<n;i++){
        fscanf(fd1,"%d",&arr[i]);
    }
    fclose(fd1);
    for(i=0;i<10;i++){
        fprintf(fd2,"%d",arr[i]);
    }
    fclose(fd2);
    return 0;
}