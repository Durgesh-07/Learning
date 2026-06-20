#include<stdio.h>
#include<stdlib.h>
typedef struct queue
{
    int data;
    queue* next;
}queue;
queue* front;queue* rear;
rear = NULL;front = NULL;
void Insert(int key){
    queue* newnode = (queue*)malloc(sizeof(queue));
    newnode->data=key;
    newnode->next=NULL;
    if(front == NULL){
        front = newnode; rear = newnode;
    }
    else{
        rear->next = newnode;
        rear = newnode;
    }
    return;
}
void Delete(){
    if(front==NULL){
        printf("Queue is Empty!!");
    }
    else{
        queue* temp = front;
        front = front->next;
        printf("%d was deleted",temp->data);
        free(temp);
    }
    return;
}
void Display(){
    if(front==NULL){
        printf("Queue is Empty!!");
        return;
    }
    queue* temp = front;
    while(temp!=NULL){
        printf("%d ",temp->data);
        temp = temp->next;
    }
    return;
}
int main(){
    int choice;
    while (1)
    {
        printf("\n\n---~Queue Basic Menu~---");
        printf("\n1. Insert");
        printf("\n2. Delete");
        printf("\n3. Display");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d",&choice);
        int ele;
        switch (choice)
        {
        case 1:
            printf("Enter what you want to insert: ");
            scanf("%d",&ele);
            Insert(ele);
            break;
        case 2:
            Delete();
            break;
        case 3:
            printf("Current Queue is: ");
            Display();
            break;
        case 4:
            printf("Terminating Program...");
            break;
        default:
            printf("Invalid Entry!! Try again.");
            break;
        }
    }
    
    return 0;
}