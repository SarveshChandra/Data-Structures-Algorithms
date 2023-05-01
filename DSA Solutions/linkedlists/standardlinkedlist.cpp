#include <iostream>

using namespace std;

class Node {
  public:
    int data; //Data to store (could be int,string,object etc)
  Node * nextElement; //Pointer to next element

  Node() {
    //Constructor to initialize nextElement of newlyCreated Node
    nextElement = nullptr;
  }
};

class LinkedList {
  private:
    Node * head;
  public:

    LinkedList();
  Node * getHead();
  bool isEmpty();
  bool printList();
  void insertAtHead(int value);
  string elements();
  void insertAtTail(int value);
  bool search(int value);
  bool deleteAtHead();
  bool Delete(int value);
  int length();
  string reverse();
  int findNth(int n);
};

LinkedList::LinkedList() {
  head = nullptr;
}

Node * LinkedList::getHead() {
  return head;
}

bool LinkedList::isEmpty() {
  if (head == nullptr) //Check whether the head points to null
    return true;
  else
    return false;
}

bool LinkedList::printList() {
  if (isEmpty()) {
    cout << "List is Empty!";
    return false;
  }
  Node * temp = head;
  cout << "List : ";

  while (temp != nullptr) {
    cout << temp->data << "->";
    temp = temp->nextElement;
  }
  cout << "null " << endl;
  return true;
}

//Function inserts a value/new Node as the first Element of list
void LinkedList::insertAtHead(int value) {
  Node * newNode = new Node();
  newNode->data = value;
  newNode->nextElement = head; //Linking newNode to head's nextNode
  head = newNode;
  cout << value << " Inserted!";
}

string LinkedList::elements() { // this function will return all values of linked List
  string elementsList = "";
  Node * start = head;

  while (start != nullptr) {
    elementsList += std::to_string(start->data);
    elementsList += "->";
    start = start->nextElement;
  }
  elementsList += "null";
  return elementsList;
}

void LinkedList::insertAtTail(int value) {
  if (isEmpty()) { // inserting first element in list
    insertAtHead(value);
  } else {
    Node * newNode = new Node();
    Node * last = head;

    while (last->nextElement != nullptr) {
      last = last->nextElement;
    }

    newNode->data = value;
    cout << value << " Inserted!    ";
    newNode->nextElement = nullptr;
    last->nextElement = newNode;
  }
}

bool LinkedList::search(int value) {
  Node * temp = head; // pointing temp to the head

  while (temp != nullptr) {
    if (temp->data == value) { // if passed value matches with temp's data
      return true;
    }
    temp = temp->nextElement; // pointig to temp's nextElement
  }
  return false; // if not found
}

bool LinkedList::deleteAtHead() {
  if (isEmpty()) { // check if lis is empty
    cout << "List is Empty" << endl;
    return false;
  }
  //if list is not empty, start traversing it from the head
  Node * currentNode = head; // currentNode pointing to head
  head = head->nextElement; //nextNode point to head's nextElement
  
  delete currentNode;
  return true;
}

bool LinkedList::Delete(int value) {
  bool deleted = false; //returns true if the node is deleted, false otherwise

  if (isEmpty()) { //check if the list is empty
    cout << "List is Empty" << endl;
    return deleted; //deleted will be false
  }

  //if list is not empty, start traversing it from the head
  Node * currentNode = head; //currentNode to traverse the list
  Node * previousNode = nullptr; //previousNode starts from null

  if (currentNode->data == value) { // deleting value of head
    deleted = deleteAtHead();
    cout << value << " deleted!" << endl;
    deleted = true; // true because value found and deleted
    return deleted; //returns true if the node is deleted
  }
  previousNode = currentNode;
  currentNode = currentNode->nextElement; // pointing current to current's nextElement
  //Traversing/Searching for Node to Delete
  while (currentNode != nullptr) {

    //Node to delete is found
    if (value == currentNode->data) {
      // pointing previousNode's nextElement to currentNode's nextElement
      previousNode->nextElement = currentNode->nextElement;
      delete currentNode;
      currentNode = previousNode->nextElement;
      deleted = true;
      break;
    }
    previousNode = currentNode;
    currentNode = currentNode->nextElement; // pointing current to current's nextElement
  }
  //deleted is true only when value is found and delted
  if (deleted == false) {
    cout << value << " does not exist!" << endl;
  } else {
    cout << value << " deleted!" << endl;
  }
  return deleted;
} 

int LinkedList::length() {
  Node * current = head; // Start from the first element
  int count = 0; // in start count is 0

  while (current != nullptr) { // Traverse the list and count the number of nodes
    count++; // increment everytime as element is found
    current = current->nextElement; // pointing to current's nextElement
  }
  return count;
}

string LinkedList::reverse() {
  Node * previous = nullptr; //To keep track of the previous element, will be used in swapping links
  Node * current = head; //firstElement
  Node * next = nullptr;

  //While Traversing the list, swap links
  while (current != nullptr) {
    next = current->nextElement;
    current->nextElement = previous;
    previous = current;
    current = next;
  }

  head = previous; // pointing head to start of the list
  return elements(); // calling elements to return a string of values in list
}

int LinkedList::findNth(int n){
    if (isEmpty()) // if list is empty return -1
    return -1;

  int length = 0;
  Node * currentNode = head; // pointing to head of the list

  // finding the length of the list
  while (currentNode != nullptr) {
    currentNode = currentNode->nextElement;
    length++;
  }

  //Find the Node which is at (len - n) position from start
  currentNode = head;
  int position = length - n;

  if (position < 0 || position > length) // check if out of the range of the list
    return -1;

  int count = 0;
  // traversing till the nth Element of the list
  while (count != position) { // finding the position of the element
    currentNode = currentNode->nextElement;
    count++;
  }

  if (currentNode != nullptr) // if node exists
    return currentNode->data;

  return -1;
}

int main() {
    LinkedList list;    //creating list
    for(int j=0; j<=7; j++) {
        list.insertAtHead(j);      //insertng data in list
        list.printList();
    }
    int num = 5;
    int nth = list.findNth(num); // calling findNth function of the list
    cout << num << "th element from end of the list : " << nth << endl;
    getchar();
    return 0;
}