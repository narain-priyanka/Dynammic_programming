# frog can jump wither i+1, i+2 and with each jump energy is consumed height[i]-height[j]
#using recursion :
height=[0,10,20,30,10]
def fj(index):
    if index<=1:
        return 1
    left= fj(index-1) + abs(height[index]-height[index-1])
    if(index>1):
        right= fj(index-2) + abs(height[index]-height[index-2])
    return min(left,right)

print(fj(4)-1)


# Using DP bottom up approach :
height=[0,10,20,30,10]
min_energy_lost=[0,0,0,0,0]
memo=[0,1,0,0,0]
def fj(index):
    if min_energy_lost[index]:
        return min_energy_lost[index]
    if index<1:
        return 0
    energy_lost_left=fj(index-1) + abs(height[index]-height[index-1])
    if(index>1):
        energy_lost_right= fj(index-2) + abs(height[index]-height[index-2])
        return min(energy_lost_left,energy_lost_right)
    return min_energy_lost[index]

print(fj(4))
