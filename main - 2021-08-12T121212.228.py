print("Welcome to Dhruv's Chemistry Calculator")
chem=str(input('Enter the calculation(no capital letters(single word)): '))

if(chem=='density'):
    mass=float(input('Enter the mass:'))
    volume=float(input('Enter the volume:'))
    density=mass/volume
    print('%0.3f is the density.' %(density))
elif(chem=='molarity'):
    moles=float(input('Enter the moles of solute:'))
    liters=float(input('Enter the liters of solution:'))
    molarity=moles/liters
    print('%0.3f is the molarity' %(molarity))
elif(chem=='energy'):
    frequency=float(input('Enter the frequency:'))
    planck=6.62607015*10^-34
    energy=frequency*planck
    print('%0.3f is the energy' %(energy))
elif(calc=='kineticenergy'):
    mass2=float(input('Enter the mass:'))
    velocity=float(input('Enter the velocity:'))
    kineticenergy=(mass2*velocity*velocity)/2
    print('%0.3f is the kinetic energy' %(kineticenergy))
elif(calc=='potentialenergy'):
    mass3=float(input('Enter the mass:'))
    height=float(input('Enter the height:'))
    gravity=9.8
    penergy=mass3*height*gravity
    print('%0.3f is the potentional energy' %(potentialenergy))
elif(calc=='wavelength'):
    mass4=float(input('Enter the mass:'))
    velocity2=float(input('Enter the height:'))
    wavelength=planck/mass4*velocity2
    print('%0.3f is the wavelength' %(wavelength))
elif(calc=='volume2'):
    pressure=float(input('Enter the pressure:'))
    volume2=1/pressure
    print('%0.3f is the volume' %(volume2))
elif(calc=='pressure2'):
    force=float(input('Enter the force:'))
    area=float(input('Enter the area:'))
    pressure2=force/area
    print('%0.3f is the pressure' %(pressure2))