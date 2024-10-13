#O txt é salvo na mesma pasta em que está o arquivo .py

with open("crescente.txt", "w") as file:
    for i in range(100):
        file.write(f"{i+1}\n")
