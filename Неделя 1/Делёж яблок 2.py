# N школьников поделили K яблок поровну, не делящийся остаток остался в корзинке. Сколько яблок осталось в корзинке?

student = int(input())
apple = int(input())
basket = apple % student
print(basket)
