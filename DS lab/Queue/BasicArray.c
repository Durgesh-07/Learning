#include<stdio.h>
#include<stdlib.h>
#define MAX 50
int rear = -1,front = -1;
int queue[MAX];
void Insert(int value){
    if(rear == MAX-1){
       printf("Overflow!!");
       return;}
    if(front == -1){
        queue[++rear]=value;front++;
    }
    else    queue[++rear]=value;;
    return;
}
void Delete(){
    if(front > rear || front ==-1){
        printf("Queue is Empty!!");
        return;
    }
    if(front==rear){
        front = -1;rear = -1;
    }
    else    front--;
    return;
}
void Display(){
    if(front > rear || front ==-1){
        printf("Queue is Empty!!");
        return;
    }
    for (int i = front; i <= rear; i++)
    {
        printf("%d ",queue[i]);
    }
    return;
}