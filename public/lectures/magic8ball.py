#######################
# Author: T Williamson
# Date: 2021-03-02
# Program: magic8ball.py
#           a program to simulate a magic 8 ball
#######################

import random

# A list full of messages received by an 8 ball
messages = [
    'It is decidedly so',
    'Yes definitely',
    'Most likely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'Better not tell you now',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful',
    'My sources say no'
    ]


def main():
    random_num = random.randint(0,len(messages)-1)
    mssg = messages[random_num]
    print(mssg)


main()
