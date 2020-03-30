import random


def start_game():

    print('>>>>>>>> Number Guessing Game <<<<<<<<')

    answer = random.randint(1, 10)
    attempt = 0
    high_score = 0

    while True:
        attempt += 1

        try:
            guess = int(input("\nPick a number between 1 to 10:   "))
            if guess > 10 or guess < 1:
                raise Exception("Ooops! Please enter only numbers between 1 to 10.")

        except ValueError:
            print("Ooops! Please enter only numbers between 1 to 10.")
            continue

        except Exception as excp:
            print(excp)
            continue

        if guess < answer:
            print("Try a higher number.")
            continue
        elif guess > answer:
            print("Try a lower number.")
            continue
        else:
            print("You got it! It took you {} attempts.".format(attempt))

            answer = random.randint(1, 10)

            high_score = attempt
            attempt = 0

            print("\nThe lowest number of attempt needed to win was {}.".format(high_score))
            more_game = input("Would you like to try again? (Y/N):   ")
            while more_game.lower() not in ("y", "n"):
                try:
                    raise ValueError("\nPlease enter 'Y' for Yes / 'N' for 'No'.")
                except ValueError as err:
                    print(err)
                more_game = input("Would you like to try again? (Y/N):   ")

            if more_game.lower() == "y":
                continue
            else:
                print("\nThanks for playing. Bye.")
                break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
