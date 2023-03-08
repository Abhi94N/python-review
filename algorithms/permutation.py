from utils import calculate_runtime

def permute(string, pocket=""):
    if len(string) == 0:
        print('pocket: ',pocket)

    else:
        #focus on the swap
        for i in range(len(string)):
            
            letter = string[i]
            print('letter: ', letter)
            front = string[0:i]
            print('front: ', front)
            back = string[i+1:]
            print('back: ', back)
            
            together = front + back
            print('together: ', together)
            permute(together, letter + pocket)
    
            


print(permute("ABCD"))
print(calculate_runtime(permute, "ABCD"))
    
    