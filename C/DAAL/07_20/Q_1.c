#include<stdio.h>
int binary(int n){
    if(n!=1){
        binary(n/2);
    }
    else{
        return 1;
    }
    if(n%2==0){
        return 0;
    }
    else{
        return 10*binary(n/2);
    }
}
int main(int argc,char* argv){
    
    return 0;
}