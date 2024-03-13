def verifier_salut(corridor):
    if not isinstance(corridor, str):
        return 0

    nombre_saluts = 0
    officiers_gauche = 0

    for char in corridor:
        if char == '>':
            officiers_gauche += 1
        elif char == '<':
            nombre_saluts += officiers_gauche

    return nombre_saluts


print(verifier_salut("->-------------<-------"))  # 1
print(verifier_salut("-<------------->-------"))  # 0
print(verifier_salut("---<---->-->----<<-->"))  # 4
print(verifier_salut("-->>----<<--"))           # 4
print(verifier_salut("--->--->----->--"))        # 0
