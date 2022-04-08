#1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
price = 3
lm = 3
bb = 5
h = 1
total_cost = price * (lm + bb + h)
print('Total cost is $' + str(total_cost))

#2.  Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
fb_hours = 10
goog_hours = 6
amz_hours = 4
fb_pay = 350
goog_pay = 400
amz_pay = 380
total_pay = (fb_hours * fb_pay + amz_hours * amz_pay + goog_hours * goog_pay)
print('Total pay is $' + str(total_pay))

#3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
is_not_full = True #or False
no_conflicts = True #or False
is_enrollable = is_not_full and no_conflicts
print(is_enrollable)

#4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
is_premium = True #or Flase
offer_expired = False #or True
no_items = 3
product_offer = (not offer_expired and no_items > 3) or is_premium
print(product_offer)
