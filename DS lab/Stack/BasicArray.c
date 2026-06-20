#include <stdio.h>
#include <stdlib.h>
#define MAX 10
int stack[MAX];
int top = -1;
void Push(int data){
    if(top == MAX-1){    printf("Stack Overflow!!");return;}
    stack[++top] = data;
    return;
}
int Ipop(){
    if(top == -1){
        printf("Stack is Empty!!");
        return;
    }
    return stack[top--];
}
void Vpop(){
    if(top == -1){
        printf("Stack is Empty!!");
        return;
    }
    top--;
    return;
}