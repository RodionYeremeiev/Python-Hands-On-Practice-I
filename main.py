# This is a sample Python script.
import Identify_palindrome
import find_all_list_items
import find_prime_factors
import sort_string
import waiting_game

# To push/pull set {git config --global http.sslVerify false} and then back to true

print(find_prime_factors.get_prime_factors(630))
print(find_prime_factors.get_prime_factors(13))
# ***
print(Identify_palindrome.is_palindrome('Hello World'))
print(Identify_palindrome.is_palindrome('Go hang a salami, I\'m a lasagna hog.'))

 # ***
print(sort_string.sort_string('zzzzzzzzzzz fffff Gggg aaaaaaaaaaa'))

# ***
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(example)
print(find_all_list_items.get_all_list_items_indexes(example, 2))

# ***
waiting_game.waiting_fame()

