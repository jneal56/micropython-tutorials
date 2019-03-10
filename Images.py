# Write your code here :-)
from microbit import *
man1 = Image("90909:""09990:""00900:""09090:""90009:")
man2 = Image("90900:""09999:""00900:""09090:""90009:")
man3 = Image("90900:""09990:""00999:""09090:""90009:")
man4 = Image("90900:""09999:""00900:""09090:""90009:")
man5 = Image("90909:""09990:""00900:""09090:""90009:")

allman = [man1, man2, man3, man4, man5]

display.show(allman, loop = False, delay=500)