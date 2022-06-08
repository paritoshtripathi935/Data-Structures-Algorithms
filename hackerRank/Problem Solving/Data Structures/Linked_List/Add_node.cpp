#include<iostream>
#include <bits/stdc++.h>
using namespace std;

class SinglyLinkedNode {  //node intilization 
    public:
        int val;
        SinglyLinkedNode* next;

    SinglyLinkedNode(int data){
        val = data;
        next = nullptr;
    }
};

class SinglyLinkedList{
    public:
        SinglyLinkedNode* head;
    
    SinglyLinkedList(){
        head = nullptr;
    }

};

void printLinkedList(SinglyLinkedNode *head){
    while(head != NULL){
        cout << head->val << endl;
        head = head->next;
    }

}

SinglyLinkedNode* insertNodeAtTail(SinglyLinkedNode* head, int data) {
    SinglyLinkedNode *n = new SinglyLinkedNode(data);
    if(head==NULL) {
        return head=n;
    }    
    else {
        SinglyLinkedNode* rhead = head;
        while(head->next != NULL){
            head = head->next;
        }
        head->next = n;
        return rhead;
    }
}

int main()
{
    SinglyLinkedList* list = new SinglyLinkedList();
    int list_count;
    cin >> list_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i = 0; i < list_count; i++) {
        int list_item;
        cin >> list_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        list->insert_node(list_item);
    }

    printLinkedList(list->head);

    return 0;
}
