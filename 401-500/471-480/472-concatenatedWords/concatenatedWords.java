class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> ans = new ArrayList<>();
        HashSet<String> wordSet = new HashSet<>(Arrays.asList(words));

        for (String word : words) if (dfs(word, wordSet))
            ans.add(word);
            
        return ans;
    }

    boolean dfs(String word, HashSet<String> wordSet) {
        for (int i = 1; i < word.length(); i++) {
            if (wordSet.contains(word.substring(0, i))) {
                String suffix = word.substring(i);
                if (wordSet.contains(suffix) || dfs(suffix, wordSet)) {
                    wordSet.add(word); // can treat concatenated word as a new word for quickly lookup later
                    return true;
                }
            }
        }

        return false;
    }
}