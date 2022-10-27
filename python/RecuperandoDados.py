import platform

print("Distribuição do S.O.:", platform.platform())
print("Nome do S.O         .:", platform.system())
print("Versão do S.O       .:", platform.release())
print("Arquitetura         .:", platform.architecture())
print("Nome do Computador  .:", platform.node())
print("Tipo de máquina     .:", platform.machine())
print("Processador         .:", platform.processor())
print("Versão do Python    .:", platform.python_version())