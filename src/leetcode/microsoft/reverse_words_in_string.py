# Source: https://leetcode.com/discuss/interview-question/1634401/Microsoft-Onsite-Interview-SDE-III
import unittest

class TestReverseWordMethod(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_words_in_string("Leetcode contains all questions"), "questions all contains Leetcode")

def reverse_words_in_string(string: str) -> str:
    list_of_words = string.split()
    list_of_words.reverse()
    return ' '.join(str(e) for e in list_of_words)

def main():
    string = "Leetcode contains all questions"
    print(reverse_words_in_string(string))

if __name__ == "__main__":
    unittest.main()


