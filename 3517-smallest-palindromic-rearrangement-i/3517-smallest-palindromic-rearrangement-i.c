char* smallestPalindrome(char* s) {
    int n = strlen(s);
    int freq[26] = {0};

    // Step 1: Count character frequencies
    for (int i = 0; i < n; i++) {
        freq[s[i] - 'a']++;
    }

    // Allocate memory for the result string (+1 for null terminator)
    char* result = (char*)malloc((n + 1) * sizeof(char));
    result[n] = '\0'; // Set null terminator at the end

    int left = 0;
    int right = n - 1;
    char mid_char = '\0';

    // Step 2: Build from 'a' to 'z' to guarantee lexicographical order
    for (int i = 0; i < 26; i++) {
        char ch = 'a' + i;

        // If the frequency is odd, identify the middle character
        if (freq[i] % 2 != 0) {
            mid_char = ch;
        }

        // Place half of the count at both ends
        int half = freq[i] / 2;
        for (int j = 0; j < half; j++) {
            result[left++] = ch;
            result[right--] = ch;
        }
    }

    // Step 3: Place the middle character if the string length is odd
    if (mid_char != '\0') {
        result[left] = mid_char;
    }

    return result;
}