#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node *left, *right;
};

// Create a new node
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Find node
void delete(struct Node* root, int value){
    if(root == NULL){
        printf("List is Empty..");
        return;
    }
    struct Node* temp = root;
    struct Node* prev = NULL;
    while(temp->data!=value){
        prev = temp;
        if(temp->data<value)    temp=temp->right;
        else    temp=temp->left;
    }
    if(temp->left==NULL && temp->right == NULL){
        prev = NULL;
        free(temp);
    }
    else if(temp->left==NULL){
        if(prev->data < temp->data){
            prev->right = findMin(temp->right);
            free(temp); 
        }
        else{
            prev->left = te
        }
    }
    return;
}

// Insert a node into BST
struct Node* insert(struct Node* root, int value) {
    if (root == NULL)
        return createNode(value);
    if (value < root->data)
        root->left = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);
    else
        printf("Duplicate value not allowed!\n");
    return root;
}

// Find minimum value node (used in deletion)
struct Node* findMin(struct Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// Traversal functions
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(struct Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

// Main Menu
int main() {
    struct Node* root = NULL;
    int choice, value;

    while (1) {
        printf("\n\n--- Binary Search Tree Menu ---\n");
        printf("1. Insert\n");
        printf("2. Inorder Traversal\n");
        printf("3. Preorder Traversal\n");
        printf("4. Postorder Traversal\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                root = insert(root, value);
                break;
            case 2:
                printf("Inorder Traversal: ");
                inorder(root);
                printf("\n");
                break;
            case 3:
                printf("Preorder Traversal: ");
                preorder(root);
                printf("\n");
                break;
            case 4:
                printf("Postorder Traversal: ");
                postorder(root);
                printf("\n");
                break;
            case 5:
                printf("Enter element you want to delete: ");
                scanf("%d",&value);
                delete(root,value);
                break;
            case 0:
                printf("Exiting program.\n");
                return 0;
            default:
                printf("Invalid choice! Try again.\n");
        }
    }
}