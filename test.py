
# Test

nom = input("Quelle est votre prénom ?")
age = int(input("Votre age ?"))
age_requis = 13


if age < 13:
    print("Bonjour " + nom + " je suis désoler mais vous ne pouvez pas entrer car vous avez " + str(age) + " ans et il faut au moins " + str(age_requis) + " ans pour entrer.")
else:
    print("Bonjour " + nom + " vous pouvez entrer car vous avez plus de " + str(age_requis) + " ans !")
