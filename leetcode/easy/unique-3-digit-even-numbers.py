class Solution:
    def totalNumbers(self, digits):
        count = [0] * 10

        # Count frequency of each digit
        for digit in digits:
            count[digit] += 1

        answer = 0

        # Choose the last digit (must be even)
        for last in range(0, 10, 2):
            if count[last] == 0:
                continue

            count[last] -= 1

            # Choose the first digit (cannot be 0)
            for first in range(1, 10):
                if count[first] == 0:
                    continue

                count[first] -= 1

                # Choose the middle digit
                for middle in range(10):
                    if count[middle] > 0:
                        answer += 1

                count[first] += 1

            count[last] += 1

        return answer