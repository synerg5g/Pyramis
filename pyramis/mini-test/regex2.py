import re

def remove_comments(code):
    # Regular expression to match single-line and multi-line comments
    pattern = r'//.*?$|/\*.*?\*/'
    cleaned_code = re.sub(pattern, '', code, flags=re.DOTALL | re.MULTILINE)
    return cleaned_code

# Example usage
code = """
#include <iostream>

// This is a single-line comment
int main() {
    /* This is a
       * multi-line
       comment */
    std::cout << "Hello, world!" << std::endl; // This is another single-line comment
    return 0;
}
"""

cleaned_code = remove_comments(code)
print(cleaned_code)
