class MyLinkedList {
private:
    //key basic data makes up the list: the node that start of the list(head node), and the size of it.
    struct Node{
        int value;
        Node* next = NULL; //pointer 
        
        Node(int data){ //constructor
            value = data;
            next = nullptr;
        }
    };
    
    Node* head;
    int size;
    
public: 
    // Intialize linked list data stucture here.
    MyLinkedList(){ 
        head = nullptr;
        size = 0;
    }
    
    // get the value of the index-th node in the linked list. if the index is invalid, return -1
    int get(int index) {
        if(index >= size || index <0){
            return -1;
        }
        else {
            Node* currentNode = head;
            for(int i=0; i<index; i++){           // gets us to the node before the index
                currentNode = currentNode->next; // moves us forward to the node of the index 
            }
            return currentNode->value;
        }
    }   
    
    // add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list
    void addAtHead(int val) {
        
    }
    
    void addAtTail(int val) {
        
    }

        /** Add a node of value val before the index-th node in the linke list. if index equals to the length of linked list, the node will be appended to the end of the linked list. if index is greater than the length, the node will not be inserted*/
    
    void addAtIndex(int index, int val) {
        if(index > size || index <0){
            return;
        }
        
        Node* newNode = new Node(val); // build a new node 
        Node* currentNode = head;
        
        if(index == 0){ // add at 0 postion 
            newNode->next = head;
            head = newNode; // assign old head to newNode
        }
        else{
            for(int i=0; i<index -1; i++){     // gets us to the node before the index
                currentNode = currentNode->next; // moves us forward to the node of the index 
            }
            newNode->next = currentNode->next;
            currentNode->next = newNode;
        }
        size++;
    }
    
    // delete the index-th node in the linked list, if the index is valid
    void deleteAtIndex(int index) {
        if(index >= size || index <0){
            return;
        }
        else if(index==0){
            Node* tempNode = head;
            head = head->next;
            delete tempNode;
        }
        else{
            Node* currentNode = head;
            
            for(int i=0; i<index-1; i++){           // gets us to the node before the index
                currentNode = currentNode->next; // moves us forward to the node of the index 
            }
            
            Node* nextNode = currentNode -> next -> next;
            delete currentNode->next;
            currentNode->next = nextNode;
        }
        size--;
    }
    
    ~MyLinkedList(){
        Node* nodeToDelete = head;
        
        while(nodeToDelete != NULL){
            head = head->next;
            delete nodeToDelete;
            nodeToDelete = head;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
