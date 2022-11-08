from sequence import digits_sequence, initialize, dec_seq
import time


initialize()    # optional - calling initialize() function will initialize the main_table and a speed up is the result!
try:
    n = int(input("Enter n number : "))
    if n < 0:
        print('n should be greater or equal 0')
        exit(0)
except ValueError:
    print('Please enter a valid number.')
    exit(0)
print("=====================================================")
print(f'Start to calculate {n} th number of sequence.')
print("=====================================================")
start = time.perf_counter()
number = digits_sequence(n)
end = time.perf_counter()
print(number)
print("=====================================================")
print(f'finished. time elapsed : {end - start} seconds.')
print("=====================================================")

# Check assertion of recursive and implemented methods
# for i in range(300):
#     main = dec_seq(i)
#     dynamic = digits_sequence(i)
#     print(f'{i} : {main} == {dynamic}')
#     assert main == dynamic
