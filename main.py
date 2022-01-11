#!/usr/bin/python3

WIDTH = 48 # Minimum width where convergence still happens
BOARD = {} # 2d array mapped to single dimension; all black at start
POSITION = 0
DIRECTION = 'N'

PATTERN = ""
TURN_PATTERN = ""
LONGEST_PATTERN = 1

turn_left = { 'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S' }
turn_right = { 'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N' }

ARROWS = { 'N': '🡡', 'E': '🡢', 'S': '🡣', 'W': '🡠' }

move_forward_delta = { 'E': +1, 'W': -1, 'N': -WIDTH, 'S': +WIDTH }
# A change to 'S': +WIDTH + 1 causes convergence to occur much sooner...

def check(pattern_length):
    i = l = len(PATTERN)-1
    while i>=pattern_length and (l-i)<pattern_length and PATTERN[i]==PATTERN[i-pattern_length]:
        i -= 1
    return (i + pattern_length) == l

# while LONGEST_PATTERN < 104:
while len(PATTERN)<10500:
    if POSITION not in BOARD or BOARD[POSITION]==False:
        DIRECTION = turn_left[ DIRECTION ]
        BOARD[POSITION] = True
        TURN_PATTERN += "1"
    else:
        DIRECTION = turn_right[ DIRECTION ]
        BOARD[POSITION] = False
        TURN_PATTERN += "0"
    POSITION += move_forward_delta[ DIRECTION ]
    print( DIRECTION, end='' )
    PATTERN += DIRECTION

    if check(104): # len(PATTERN)>1000 and
        print( f"Found after {len(PATTERN)} steps" )
        print( PATTERN[-104:] )
        print( TURN_PATTERN[-104:] )
        for c in PATTERN[-104:]:
            print( ARROWS[c], end='' )
        break

    # Find the longest pattern that does not repeat itself
    # if len(PATTERN)%100 == 0:
    #  check_pattern_length = min( int( len(PATTERN) / 3 ), 104 )
    #  while check_pattern_length>LONGEST_PATTERN:
    #   i = len(PATTERN) - 1
    #   while (i>=2*check_pattern_length
    #          and PATTERN[i] == PATTERN[i-check_pattern_length]
    #          and PATTERN[i] != PATTERN[i-2*check_pattern_length]):
    #     i = i-1
    #   if (len(PATTERN) - 1 - i) == check_pattern_length:
    #       LONGEST_PATTERN = len(PATTERN) - 1 - i
    #       print( f"New max pattern of length {LONGEST_PATTERN} after { len(PATTERN) }: {PATTERN[-LONGEST_PATTERN:]}" )
    #       print( PATTERN[-3*LONGEST_PATTERN:] if len(PATTERN)>80 else PATTERN )
    #       break
    #   check_pattern_length = check_pattern_length - 1
