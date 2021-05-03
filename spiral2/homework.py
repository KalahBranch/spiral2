def spiralize(size, n=1):
    return_value = (
        n  # Setting it equal to n, since n will be the first number in the diagoal
    )
    starting_Number = n
    turn = 2  # We will increment this as we turn in each part of the matrix
    steps = 0

    while starting_Number < (size * size + n - 1):
        starting_Number = starting_Number + turn
        return_value = return_value + starting_Number
        steps = steps + 1

        if steps == 4:
            turn += 2  # Found a pattern in which each time I go around the diagonal "new loop" after storing 4 values, we increase by 2
            steps = 0

    #    6 * * * * * 6
    #    * 4 * * * 4 *
    #    * * 2 * 2 * *
    #    * * * 0 * * *
    #    * * 2 * 2 * *
    #    * 4 * * * 4 *
    #    6 * * * * * 6
    return return_value


print(spiralize(1, 35))
print(spiralize(11, 27))
print(spiralize(21, 28))
print(spiralize(2, 35))

# assert homework.spiralize(1, 35) == 35
# assert homework.spiralize(11, 27) == 1507
# assert homework.spiralize(21, 28) == 7528
