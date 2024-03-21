altura = float(input("Informe sua altura: "))
genero = input("Você é homem ou mulher: ").lower()
if genero == "homem":
    print(f"Seu peso ideal é {(72.7*altura)-58:.2f} kg")
elif genero == "mulher":
    print(f"Seu peso ideal é {(62.1*altura)-44.7:.2f} kg")
