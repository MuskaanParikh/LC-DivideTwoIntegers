def divide(dividend: int, divisor: int) -> int:
    quotient = 0
    sign = (dividend < 0) != (divisor < 0)
    if dividend == 0 or divisor == 0: return 0

    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if sign: 
        quotient = 0 - quotient 

    return quotient 

print(divide(10,3))
print(divide(7,-3))
print(divide(-1,-1))