class Solution: 
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        n_digits = len(num_str)
        romans = {"1": "I", "5": "V", "10": "X", "50": "L", "100": "C", "500": "D", "1000": "M"}

        helper_map = {
            4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"
        }
        # 2376 -> n_digits = 4
        ans = ""
        for i in range(n_digits):
            digit_i = int(num_str[i]) 
            val = digit_i * pow(10,n_digits-1-i)
            if digit_i!=4 and digit_i!=9 :
                max_key_subtractable = None
                while val:
                    for key in romans.keys():
                        if val-int(key) >= 0:
                            max_key_subtractable = key
                    if max_key_subtractable:
                        val -= int(max_key_subtractable)
                        ans += romans[max_key_subtractable]
            else:
                ans+= helper_map[val]

        return ans
