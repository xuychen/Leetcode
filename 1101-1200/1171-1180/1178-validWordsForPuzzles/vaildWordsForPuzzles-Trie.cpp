#include <algorithm>
#include <string>
#include <vector>
#include <set>

#define ALPHABET_SIZE 26

using namespace std;

/* The structure of a trie node */
class TrieNode {
    TrieNode* children[ALPHABET_SIZE];
    int count;
  public:
    TrieNode();
    int search(string &str, char firstLetter);

    friend class TrieTree;
};

class TrieTree {
    TrieNode *root;
  public:
    TrieTree ();
    void insert(string &str);
    int search(string &str, char firstLetter);
};

/* Creates a new trie node and returns the pointer */
TrieNode::TrieNode(): count(0) {
    for (int i = 0; i < ALPHABET_SIZE; ++i)
        children[i] = NULL;
}

int TrieNode::search(string &str, char firstLetter) {
    int result = 0;


    if (!firstLetter)
        result += count;

    for (int i = 0; i < str.length(); i++) {
        int index = str[i] - 'a';
        if (children[index])
            result += children[index]->search(str, str[i] == firstLetter ? '\0' : firstLetter);
    }

    return result;
}

TrieTree::TrieTree() {
    root = new TrieNode();
}

/* Inserts the given string to the collection */
void TrieTree::insert(string &str) {
    TrieNode *node = root;
    for (int i = 0; i < str.length(); i++) {
        int index = str[i] - 'a';
        if (!node->children[index])
            node->children[index] = new TrieNode();

        node = node->children[index];
    }

    node->count++;
}

/* Returns the count of strings which are valid */
int TrieTree::search(string &str, char firstLetter) {
    return root ? root->search(str, firstLetter) : 0;
}

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        TrieTree trie;

        for (auto str : words) {
            set<char> temp;
            temp.insert(str.begin(), str.end());

            string sorted = "";
            for (auto ele : temp)
                sorted += ele;

            trie.insert(sorted);
        }

        vector<int> count;
        for (auto puzzle : puzzles) {
            char firstLetter = puzzle[0];
            sort(puzzle.begin(), puzzle.end());
            count.push_back(trie.search(puzzle, firstLetter));
        }

        return count;
    }
};