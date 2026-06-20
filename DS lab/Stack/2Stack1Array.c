#include <stdio.h>
#include <stdlib.h>
#define MAX 10
int stack[MAX];
int top1 = -1;
int top2 = MAX/2-1;
void Pusk1(int value){
    if(top1 == MAX/2-1)  {
        printf("Stack1 overflow!!");
        return;
    }
    stack[++top1];
    return;
}
void Pusk2(int value){
    if(top2 == MAX-1)  {
        printf("Stack2 overflow!!");
        return;
    }
    stack[++top2];
    return;
}
int Ipop1(){
    if(top1 == -1){
        printf("Stack is Empty!!");
        return;
    }
    return stack[top1--];
}
void Vpop1(){
    if(top1 == -1){
        printf("Stack is Empty!!");
        return;
    }
    top1--;
    return;
}
int Ipop2(){
    if(top2 == MAX/2-1){
        printf("Stack is Empty!!");
        return;
    }
    return stack[top2--];
}
void Vpop2(){
    if(top2 == MAX/2-1){
        printf("Stack is Empty!!");
        return;
    }
    top2--;
    return;
}