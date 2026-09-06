username = "python"
password = "rules"
attempts = 0

while attempts < 5:

    given_username = input("Anna käyttäjänimi: ")
    given_pwd = input("Anna salasana: ")

    if given_username != username or given_pwd != password:
        attempts += 1
        print("Käyttäjänimi tai salasana väärin.")
    else:
        print("Tervetuloa.")
        break
else:
    print("Pääsy evätty.")