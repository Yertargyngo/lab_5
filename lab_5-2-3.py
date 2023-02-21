list = []
san = int(input("Кез келген бүтін сан жазыңыз: (Жазуды тоқтату үшін 0-ді жазу керек): "))
while san != 0:
    list.append(san)
    san = int(input("Кез келген бүтін сан жазыңыз: (Жазуды тоқтату үшін 0-ді жазу керек): "))
print(*sorted(list), sep='\r\n')