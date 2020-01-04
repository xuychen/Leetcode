#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

#define ASCIIa 97

using namespace std;

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        vector<int> result;

        for (string &puzzle: puzzles) {
            int count = 0;
            unordered_set<char> hashTable;

            for (char chr: puzzle)
                hashTable.insert(chr);

            for (string &word: words) {
                bool successFlag = true;
                if (word.find(puzzle[0]) == string::npos)
                    continue;

                for (char wordChr: word)
                    if (hashTable.find(wordChr) == hashTable.end()) {
                        successFlag = false;
                        break;
                    }

                if (successFlag)
                    ++count;
            }

            result.push_back(count);
        }

        return result;
    }

    vector<int> findNumOfValidWords2(vector<string>& words, vector<string>& puzzles) {
        vector<int> result;
        unordered_map<int, int> encodedWords;

        for (string &word: words) {
            int encodedWord = stringEncoding(word);
            encodedWords.emplace(encodedWord, 0);
            ++encodedWords[encodedWord];
        }

        for (string &puzzle: puzzles) {
            int count = 0;
            int encodedPuzzle = stringEncoding(puzzle), firstCharEncoding = charEncoding(puzzle[0]);

            for (int subPuzzle = encodedPuzzle; subPuzzle; subPuzzle = (subPuzzle - 1) & encodedPuzzle)
                if ((subPuzzle & firstCharEncoding) == firstCharEncoding && encodedWords.find(subPuzzle) != encodedWords.end())
                    count += encodedWords[subPuzzle];

            result.push_back(count);
        }

        return result;
    }

    int charEncoding(char c) {
        return 1 << (c - ASCIIa);
    }

    int stringEncoding(string s) {
        int result = 0;
        for (char c: s)
            result |= charEncoding(c);

        return result;
    }
};