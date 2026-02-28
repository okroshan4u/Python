print("Hello wolrd !"

def tell(n):
    print(n)

tell("Roshan")    
# Jitna bhi data ka type hai uo memory main jata na ki variable k pass jata ha
# matlab , python ka datatypes nahi hot hai matlab python main koi datatype nahi hota hai 
# matlab vaiable ka datatype nahi hot lekin uska jo reference hota that 
# is what ever be the value that is referencing to that variable that 
# will have the data type in the memory
#   [score] 
#       |
#       |----------------------.
#       |                      |   __> it will have the datatype not the score variable 
#   [a_score]                  v  |
#       |                 +-----------+
#       '---------------->|     10    |   ref_count
#                         +-----------+
#                               |
#                               |
#                               v
#                         +-----------+
#                         |           |
#                         |           |
#                         |           |
#                         |           |
#                         +-----------+

#   [     ]  ...............................>
#                     |
#                     v
#               +-----------+
#               |           |
#               +-----------+


