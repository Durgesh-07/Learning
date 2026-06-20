#include<stdio.h>
#include<stdlib.h>
#define MAX 10
int front = -1,rear = -1;
int queue[MAX];
void Insert(int value){
    if(rear+1 == front || (front == 0 && rear == MAX-1)){
        printf("Overflow!!");
        return;
    }
    if(front == -1 && rear == -1){
        queue[++rear]=value;front++;
    }
    else if(rear == MAX-1){
        rear = 0;queue[rear] = value;
    }
    else    queue[++rear]=value;
    return;
}
void Delete(){
    if(front == -1){
    printf("Queue is Empty!!");
    return;
    }
    if(front == MAX-1){
        front = 0;
    }
    else if(front == rear){
        front = 0;rear = 0;
    }
    else{
        front++;
    }
    return;
}
void Display(){
    if(front == -1){
        printf("Queue is Empty!!");
        return;
    }
    if(front <= rear){
        for (int i = front; i <= rear; i++) printf("%d ",queue[i]);
    }
    else{
        for (int i = front; i <= MAX-1; i++)
        {
            printf("%d ",queue[i]);
        }
        for (int i = 0; i <= rear; i++)
        {
            printf("%d ",queue[i]);
        }
    }
}