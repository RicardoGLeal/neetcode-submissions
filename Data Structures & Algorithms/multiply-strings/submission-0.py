class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2

                lowPos = i + j + 1
                highPos = i + j

                total = res[lowPos] + product

                res[lowPos] = total % 10
                res[highPos] += total // 10
        res_str = ''.join(map(str, res))
        return res_str.lstrip('0') or "0"
