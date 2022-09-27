# This is a sample Python script.
import time

import Exercise_6
import Identify_palindrome
import exercise7
import find_all_list_items
import find_prime_factors
import sort_string
import waiting_game

# To push/pull set {git config --global http.sslVerify false} and then back to true

print(find_prime_factors.get_prime_factors(630))
print(find_prime_factors.get_prime_factors(13))
print('*********')
print(Identify_palindrome.is_palindrome('Hello World'))
print(Identify_palindrome.is_palindrome('Go hang a salami, I\'m a lasagna hog.'))

print('*********')
print(sort_string.sort_string('zzzzzzzzzzz fffff Gggg aaaaaaaaaaa'))

print('*********')
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(example)
print(find_all_list_items.get_all_list_items_indexes(example, 2))

print('*********')
# waiting_game.waiting_game()

print('*********')
test_dict = {1: 'a', 2: 'b', 3: 'c'}
Exercise_6.save_dict(test_dict, 'test_dict.pickle')
recovered = Exercise_6.load_dict('test_dict.pickle')
print(recovered)

print('*********')

exercise7.set_alarm(time.time()+1, '5_46B.wav', 'Wake up!')
