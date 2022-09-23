# This is a sample Python script.
import Identify_palindrome
import find_prime_factors
import sort_string

# To push/pull set {git config --global http.sslVerify false} and then back to true

print(find_prime_factors.get_prime_factors(630))
print(find_prime_factors.get_prime_factors(13))

print(Identify_palindrome.is_palindrome('Hello World'))
print(Identify_palindrome.is_palindrome('Go hang a salami, I\'m a lasagna hog.'))

print(sort_string.sort_string('zzzzzzzzzzz fffff Gggg aaaaaaaaaaa'))
