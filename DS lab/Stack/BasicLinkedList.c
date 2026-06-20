#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
typedef struct Stack{
    int info;
    struct Stack* prev;
}Stack;
Stack* Top = NULL;
void Push(int key){
    Stack* newnode;
    newnode = (Stack*)malloc(sizeof(Stack));
    newnode->info = key;
    newnode->prev = Top;
    Top = newnode;
    return;
}
void Pop(){       // only top node is deleted
    if(Top==NULL)   return;
    else{
        int item = Top->info;
        Stack* Temp = Top;
        Top = Top->prev;
        Temp->prev = NULL;
        free(Temp);
        printf("%d was deleted\n",item);
    }
    return;
}
int Peek(){
    return Top->info;
}
bool IsEmpty(){
    if(Top == NULL)  return true;
    else    return false; 
}
void Display(){
    if(Top==NULL)   return;
    Stack* Temp;
    Temp = Top;
    while (Temp!=NULL)
    {
        printf("%d ",Temp->info);
        Temp=Temp->prev;
    }
    return;
}
int main(){
    while (1)
    {
        printf("\n\n--- Stack Basic Menu ---");
        printf("\n1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Display\n");
        printf("5. Exit\n");int choice,item;
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("Enter what you want to push: ");
            scanf("%d",&item);
            Push(item);
            break;
        case 2:
            Pop();
            break;
        case 3:
            printf("Top is %d\n",Peek());
            break;
        case 4:
            Display();
            printf("\n");
            break;
        case 5:
            printf("Exiting program.\n");
            return 0;
        default:
            printf("Invalid Choice!! Try again.\n\n");
            break;
        }
    }
}