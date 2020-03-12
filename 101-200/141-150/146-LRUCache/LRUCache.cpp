#include <unordered_map>

using namespace std;

class Node {
    Node *prev;
    Node *next;
    int key;
    int value;
public:
    Node(int _key, int _value): prev(nullptr), next(nullptr), key(_key), value(_value) {};
    int getKey();
    int getValue();
    friend class DoublyLinkedList;
};

int Node::getKey() {
    return key;
}

int Node::getValue() {
    return value;
}

class DoublyLinkedList {
    Node *head;
    Node *end;
    int length;
public:
    DoublyLinkedList() : head(nullptr), end(nullptr), length(0) {};
    void insertHead(Node *node);
    void remove(Node *node);
    void update(Node *node, int value);
    Node *getHead();
    Node *getEnd();
    int size();
};

void DoublyLinkedList::insertHead(Node *node) {
    if (head)
        head->prev = node;
    else
        end = node;
    
    node->prev = nullptr;
    node->next = head;
    head = node;
    ++length;
}

void DoublyLinkedList::remove(Node *node) {
    if (node->prev)
        node->prev->next = node->next;
    else {
        head = node->next;
        if (head)
            head->prev = nullptr;
    }

    if (node->next)
        node->next->prev = node->prev;
    else {
        end = node->prev;
        if (end)
            end->next = nullptr;
    }
    
    --length;
}

void DoublyLinkedList::update(Node *node, int value) {
    node->value = value;
}

Node *DoublyLinkedList::getHead() {
    return head;
}

Node *DoublyLinkedList::getEnd() {
    return end;
}

int DoublyLinkedList::size() {
    return length;
}

class LRUCache {
    int capacity;
    unordered_map<int, Node*> hashMap;
    DoublyLinkedList linkedList;
public:
    LRUCache(int _capacity): capacity(_capacity) {};
    
    int get(int key) {
        auto iter = hashMap.find(key);
        if (iter == hashMap.end())
            return -1;

        linkedList.remove(iter->second);
        linkedList.insertHead(iter->second);
        return iter->second->getValue();
    }
    
    void put(int key, int value) {
        auto iter = hashMap.find(key);
        if (iter != hashMap.end()) {
            linkedList.update(iter->second, value);
            linkedList.remove(iter->second);
            linkedList.insertHead(iter->second);
        }
        else {
            linkedList.insertHead(new Node(key, value));
            hashMap[key] = linkedList.getHead();
        }

        if (linkedList.size() == capacity + 1) {
            Node *node = linkedList.getEnd();
            linkedList.remove(node);
            hashMap.erase(node->getKey());
            delete node;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */