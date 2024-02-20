from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        L = []
        for i in range(1, n+1):
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0
            if (divisibleBy3) & (divisibleBy5):
                L.append('FizzBuzz')
            elif divisibleBy3:
                L.append('Fizz')
            elif divisibleBy5:
                L.append('Buzz')
            else:
                L.append(str(i))
        return L


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        L = []

        for i in range(1, n+1):

            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0

            string = ''

            if divisibleBy3:
                string += 'Fizz'

            elif divisibleBy5:
                string += 'Buzz'

            else:
                string += str(i)

            L.append(string)

        return L


print(
    Solution().fizzBuzz(5)  # Output: ["1","2","Fizz","4","Buzz"]
)
