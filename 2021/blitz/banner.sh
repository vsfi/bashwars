#!/bin/sh
echo "
####################################
#                                  #
#              BLITZ!              #
#                                  #
####################################

I'm thinking of a number. It is in bw_numbers.txt. The first digit is not 5. The second digit is 5 for sure. Then something between 2 and 4. And definetely 1 in the end.

I'm thinking of a name. It is in bw_names.txt, starts with capital vowel, then some letter, then o, then some more letters and i in the end.

I'm thinking of gender. It is in bw_genders.txt and it contains at least two words. The word woman is in the end and in summary there're 4 letters a and three letters r.

Wanna get a flag? Run ./runner number name gender
"
if [ "$USER" != "blitz" ]; then
    cd /home/blitz
    su blitz -c "sh"
fi
