'''
program use Ohm's law to calculate the resistance. User gives voltage and current
'''
voltage = int(input("Voltage:"))
current = int(input("Current: "))

resistance = voltage / current

print(resistance)