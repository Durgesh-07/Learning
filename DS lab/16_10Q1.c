#include <stdio.h>
#include <stdlib.h>
struct level
{
    int info;
    struct level* prev;
};

typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} node;

node* newTree() {
    int data;
    printf("Enter data: ");
    scanf("%d", &data);

    node* newNode = (node*)malloc(sizeof(node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    newNode->data = data;
    char c;
    printf("left %d? (y/n): ", data);
    scanf(" %c", &c);
    if (c == 'y')
        newNode->left = newTree();
    else
        newNode->left = NULL;
    printf("right %d? (y/n): ", data);
    scanf(" %c", &c);
    if (c == 'y')
        newNode->right = newTree();
    else
        newNode->right = NULL;

    return newNode;
}

// void preOrder(node* Tree) {
//     if (Tree == NULL) return;
//     printf("[%d]", Tree->data);
//     preOrder(Tree->left);
//     preOrder(Tree->right);
// }
void preOrder(node* Tree){
    if(Tree == NULL)    return;
    node* curr;
    curr = Tree;
    return;
}
void inOrder(node* Tree) {
    if (Tree == NULL) return;
    preOrder(Tree->left);
    printf("[%d]", Tree->data);
    preOrder(Tree->right);
}

void postOrder(node* Tree) {
    if (Tree == NULL) return;
    preOrder(Tree->left);
    preOrder(Tree->right);
    printf("[%d]", Tree->data);
}

void freeTree(node* Tree) {
    if (Tree == NULL) return;
    freeTree(Tree->left);
    freeTree(Tree->right);
    free(Tree);
}

int main() {
    node* Tree = newTree();

    printf("1. PreOrder\n");
    printf("2. InOrder\n");
    printf("3. PostOrder\n");
    printf("0. Exit\n");

    int c;

    while(1){
        printf("choice: ");
        scanf("%d", &c);

        if(c==1) {
            preOrder(Tree);
            printf("\n");
        }
        else if(c==2) {
            inOrder(Tree);
            printf("\n");
        }
        else if(c==3) {
            postOrder(Tree);
            printf("\n");
        }
        else if(c==0) {
            printf("GoodBye");
            break;
        }
        else printf("try again\n");

    }


    freeTree(Tree);
    return 0;
}