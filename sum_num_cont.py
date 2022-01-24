#!/usr/bin/env python3

# Created by Dylan Melo
# Created Jan, 2022
# Program asks the user the amount of numbers they want to add
# together. Then, uses a while loop to calculate and display
# the sum of the numbers.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0
    answer = ""

    while True:
        # get user number as a string
        user_num_a_str = input("Add as many numbers as you want: ")
        print("")

        try:
            # converts the first user input to integer
            user_num_a_int = int(user_num_a_str)

            if user_num_a_int >= 0:
                # calculate the sum of the entered numbers
                while (loop_counter < user_num_a_int):
                    # gets input from user
                    user_num_b_str = input("Enter a number: ")

                    try:
                        # converts entered number from string to integer
                        user_num_b_int = int(user_num_b_str)
                        # joins the strings

                        if user_num_b_int < 0:
                            print("{} is < 0 and cannot be added"
                                  .format(user_num_b_int))
                            print("")
                            continue

                        print()
                        print("{} added to the sum."
                              .format(user_num_b_int))
                        print("")
                        sum = sum + user_num_b_int
                        loop_counter = loop_counter + 1
                        answer += str(user_num_b_int) + " + "
                    except Exception:
                        print("{} is not a number.". format(user_num_b_str))
                        print("")
                        continue
                if loop_counter == user_num_a_int:
                    print("{}0 = {} " .format(answer, sum))
                    print("The sum is {}.".
                          format(sum))
                    break
            else:
                print("Please enter a whole number!")
                print("")
        except Exception:
            print("{} is not a number.". format(user_num_a_str))
            print("")


if __name__ == "__main__":
    main()
