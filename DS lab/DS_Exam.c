#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node* next;
};
struct node* head = NULL;
void create(int value){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    if(head == NULL){
        head = newnode;
        newnode->next = newnode;
    }
    else if(head->next == head){
        head->next = newnode;
        newnode->next = head;
    }
    else{
        struct node* ptr = head;
        while(ptr->next != head){
            ptr = ptr->next;
        }
        ptr->next = newnode;
        newnode->next = head;
    }
}
void display(){
    if(head == NULL){
        printf("List is Empty!");
        return;
    }
    struct node* ptr = head;
    while (ptr->next != head)
    {
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
    printf("%d \n",ptr->data);
    return;
}
int main(){
    printf("Enter no. of elements you want in list: ");
    int no;
    scanf("%d",&no);
    int value;
    for (int  i = 0; i < no; i++)
    {
        printf("Enter value: ");
        scanf("%d",&value);
        create(value);
    }
    printf("\nYour circular list is: ");
    display();
    return 0;
}