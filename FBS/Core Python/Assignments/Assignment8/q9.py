def checkPallindrome(num): 
    original = num
    rev = 0           

    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10

    if rev == original:
        print('Palindrome Number')
    else:
        print('Not a Palindrome Number')

checkPallindrome(121)