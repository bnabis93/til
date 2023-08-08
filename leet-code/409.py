


def longest_palindrome(s: str) -> int:
    length_s = len(s)
    if length_s == 1:
        return 1
    
    ans = 0 
    set_s = set(s)
    if len(set_s) ==1:
        num2 = length_s // 2
        print("num : ", num2)
        ans += (num2 * 2)
        if num2 ==1:
            print("??")
            ans +=1
        print(f"ans : {ans}")
        return ans

    ans = 0
    flag = False
    for char in set_s:
        num_of_char_in_s = s.count(char)
        num2 = num_of_char_in_s // 2
        ans += (num2 * 2)
        if num2 == 0 and flag == False:
            flag = True
            ans += 1

    print(f"ans : {ans}")


longest_palindrome(s = "abccccdd")
longest_palindrome(s = "ccc")
longest_palindrome(s = "bb")


