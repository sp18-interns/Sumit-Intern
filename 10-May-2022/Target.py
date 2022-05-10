def vishal_sir_Quiz(List_1, Target):
    for i in range(len(List_1) - 1):
        for j in range(i + 1, len(List_1)):
            if List_1[i] + List_1[j] == Target:
                print(f" the two numbers are {List_1[i]} & {List_1[j]}")
                print(f" Target = {Target} is equal to {List_1[i] + List_1[j]}")
vishal_sir_Quiz([3,2,1,4], 5)
