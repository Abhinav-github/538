'''
Earlier this year, a new generation of Brood X cicadas had emerged in many parts of the U.S. This particular brood emerges every 17 years,
while some other cicada broods emerge every 13 years. Both 13 and 17 are prime numbers — and relatively prime with one another — which
means these broods are rarely in phase with other predators or each other. In fact, cicadas following a 13-year cycle and cicadas following
 a 17-year cycle will only emerge in the same season once every 221 (i.e., 13 times 17) years!

Now, suppose there are two broods of cicadas, with periods of A and B years, that have just emerged in the same season. However, these
two broods can also interfere with each other one year after they emerge due to a resulting lack of available food. For example, if A
is 5 and B is 7, then B’s emergence in year 14 (i.e., 2 times 7) means that when A emerges in year 15 (i.e., 3 times 5) there won’t
be enough food to go around.

If both A and B are relatively prime and are both less than or equal to 20, what is the longest stretch these two broods can go without
interfering with one another’s cycle? (Remember, both broods just emerged this year.) For example, if A is 5 and B is 7, then the
interference would occur in year 15.
'''

if __name__ == "__main__":
    prime_numbers = [2,3,5,7,11,13,17,19]
    year_periods = [[] for i in range(len(prime_numbers))]
    #print(year_periods)
    for index, prime in enumerate(prime_numbers):
        for period in range(1, 50):
            cur_year = prime*period
            year_periods[index].append(cur_year)
            year_periods[index].append(cur_year + 1)
    #print(year_periods)
    unique = [[] for i in range(len(prime_numbers))]
    for i in range(len(year_periods)):
        for j in range(i+1,len(year_periods)):
            for A in year_periods[i]:
                if A in year_periods[j]:
                    unique[i].append(A)
                    break
    min_array = []
    #print(unique)
    for i in unique:
        if i:
            min_array.append(min(i))
    #print(min_array)
    print(max(min_array))
