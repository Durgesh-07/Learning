#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node* next;
}Stack;
struct Node* top = NULL;
int isEmpty(struct Node* top) {
if (top == NULL)

return 1;
else

return 0;
}
void push(int value) {
struct Node* node;

node=(struct stack *)malloc(sizeof(struct Node));

node->data=value;
if (top == NULL) {
top=node;

top->next=NULL;

}

else {

node->next=top;
top=node;

}
return;
}
int Pop() {

int item;
struct Node* temp;

if( top == NULL) {

printf(" Empty Stack …");

return -1;

}

else {

temp=top;
item=top->data;
top=top->next;

temp->next=NULL;
free(temp);
return(item);

}

}
int peak(struct Node* top) {
struct Node* temp;

temp = top;

if (top == NULL) {

printf("Empty stack …");

return -1;

}

else {

return top->data;

}

}
struct branch {
int data;
struct branch* left;
struct branch* right;
};
struct branch* createTree() {

int data;

printf("Enter data (-1 for NULL): ");

scanf("%d", &data);

// Base case

if (data == -1)

return NULL;

// Create a new node

struct branch* newNode = (struct branch*)malloc(sizeof(struct branch));

newNode->data = data;

// Recursively create left and right subtrees

printf("Enter left child of %d\n", data);

newNode->left = createTree();

printf("Enter right child of %d\n", data);

newNode->right = createTree();

return newNode;

}
void displayPreord(struct Node* root){
    struct branch* curr = root;
    push(curr);
    while (top!=NULL)
    {
        curr = pop();
        printf("%d",curr->data);
        if(curr->left!=NULL)
            push(curr->left);
        if(curr->right!=NULL)
            push(curr->right);
    }
    return;
}
void displayInord(struct Node* root){
    struct branch* curr = root;
    
    while (top!=NULL || -isEmpty(top))
    {
        curr = pop();
        printf("%d",curr->data);
        if(curr->left!=NULL)
            push(curr->left);
        if(curr->right!=NULL)
            push(curr->right);
    }
    return;
}