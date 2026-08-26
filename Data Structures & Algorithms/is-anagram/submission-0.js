class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let letters = {};
        for (let char of s) {
            if (!(char in letters)) letters[char] = 0;
            letters[char]++;
        }

        for (let char of t) {
            if (!(char in letters)) return false;
            letters[char]--;
            if (letters[char] == 0) delete(letters[char]); 
        }
        console.log()
        return Object.keys(letters).length == 0;
    }
}
