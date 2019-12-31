#include <vector>

using namespace std;

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int result = 0;

        for (int i = 0; i < board.size(); ++i)
            for (int j = 0; j < board[i].size(); ++j) {
                if (board[i][j] != 'X')
                    continue;

                int result1 = checkDownward(board, i, j);
                int result2 = checkRightward(board, i, j);
                if ((result1 == 2 || result2 == 2) && (result1 == 1 && result2 == 1))
                    return 0;
                else
                    ++result;
            }

        return result;
    }

    int checkDownward(vector<vector<char>> &board, int i, int j){
        int newi = i + 1;
        for (; newi < board.size(); ++newi)
            if (board[newi][j] == 'X' && (j == 0 || board[newi][j-1] != 'X') && (j == board[newi].size() - 1 || board[newi][j+1] != 'X'))
                board[newi][j] = 'x';
            else if (board[newi][j] != 'X')
                break;
            else
                return 2;


        return newi != i + 1;
    }

    int checkRightward(vector<vector<char>> &board, int i, int j){
        int newj = j + 1;
        for (; newj < board[i].size(); ++newj)
            if (board[i][newj] == 'X' && (i == 0 || board[i-1][newj] != 'X') && (i == board.size() - 1 || board[i+1][newj] != 'X'))
                board[i][newj] = 'x';
            else if (board[i][newj] != 'X')
                break;
            else
                return 2;

        return newj != j + 1;
    }
};