from random import choice
import requests as req
normal_color = "\033[0;31m"
info_color = "\033[0;31m"
red_color = "\033[0;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[0;31m"
detect_color = "\033[0;31m"
banner_color = "\033[0;39m"
end_banner_color = "\033[0;31m"
print(detect_color+'''
              █████████   █████                   █████                                                
  ███░░░░░███ ░░███                   ░░███                                                 
 ░███    ░███  ░███████  █████ ████    ░███         ██████   █████ ████  ██████   ████████  
 ░███████████  ░███░░███░░███ ░███     ░███        ░░░░░███ ░░███ ░███  ░░░░░███ ░░███░░███ 
 ░███░░░░░███  ░███ ░███ ░███ ░███     ░███         ███████  ░███ ░███   ███████  ░███ ░███ 
 ░███    ░███  ░███ ░███ ░███ ░███     ░███      █ ███░░███  ░███ ░███  ███░░███  ░███ ░███ 
 █████   █████ ████████  ░░████████    ███████████░░████████ ░░███████ ░░████████ ████ █████
░░░░░   ░░░░░ ░░░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░   ░░░░░███  ░░░░░░░░ ░░░░ ░░░░░ 
                                                              ███ ░███                      
                                                             ░░██████                       
                                                              ░░░░░░                        
          
''')

print('''
##### ##### ##### ##### ##### ##### ##### ##### ##### #####                                                                                                                                                                                                                                                 
		developer : Abu Layan
		developer_snapchat : devadnan            
		                                                                                                            
##### ##### ##### ##### ##### ##### ##### ##### ##### #####  
''')


print('')

Q = int(input(green_color+'''

[+] SnapChat : Enter Number 1

[+] Tiktok : Enter Number 2

[+] Twitter : Enter Number 3


[+] Your Choises Here ==> '''))

if Q == 1:
    Q1 = input(green_color+"You Want Search For Spcfivc User (yes/no) ==> ")
    print("\n")
    if Q1 == "no":
        print(banner_color+"Ex : Enter how many users you want ==>  100")
        print("\n")
        users = int(input(green_color + "Enter how many users you want ==> "))
        print("\n")
        print(banner_color+"Ex : Enter how many users you want ==>  3")
        let_user = int(
            input(green_color + "Enter how many letter user you want ==> "))
        print("\n")

        for i in range(users):
            def gnretorusers(let_user):
                user = ''
                letter = "qwertyuiopasdfghjklzxcvbnm"

                for i in range(let_user):
                    user += choice(letter)
                return user
            with open('users_snapchat.txt', 'w') as f:
                for i in range(users):
                    f.write(gnretorusers(let_user))
                    f.write("\n")
                    f.close
        file1 = open('users_snapchat.txt', 'r')
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            # print(line.strip())
            usercheck = line.strip()
            checker = req.get(f"https://www.snapchat.com/add/{usercheck}")
            if checker.status_code == 200:
                print(detect_color+"unavailable ==> " +
                      f"https://www.snapchat.com/add/" + usercheck)
            else:
                print(green_color+"available ==> " +
                      f"https://www.snapchat.com/add/" + usercheck)
        print("\n")
        print("\n")
        print(detect_color + "Message From Abu Layan")
        print(green_color + "Thanks For Useing My Script \n Bye")
    elif Q1 == "yes":
        UserfromClint = input(green_color+"Enter the username ==> ")
        print("\n")
        print("\n")
        checker2 = req.get(f"https://www.snapchat.com/add/{UserfromClint}/")
        if checker2.status_code == 200:
            print(detect_color+"unavailable ==> " +
                  f"https://www.snapchat.com/add/" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
        else:
            print(green_color+"available ==> " +
                  f"https://www.snapchat.com/add/" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
    else:
        print("You did not choose correct \n Bye")
elif Q == 2:
    Q1 = input(green_color+"You Want Search For Spcfivc User (yes/no) ==> ")
    print("\n")
    if Q1 == "no":
        print(banner_color+"Ex : Enter how many users you want ==>  100")
        print("\n")
        users = int(input(green_color + "Enter how many users you want ==> "))
        print("\n")
        print(banner_color+"Ex : Enter how many users you want ==>  3")
        let_user = int(
            input(green_color + "Enter how many letter user you want ==> "))
        print("\n")

        for i in range(users):
            def gnretorusers(let_user):
                user = ''
                letter = "qwertyuiopasdfghjklzxcvbnm"
                number = "1234567890"
                for i in range(let_user):
                    user += choice(letter + number)
                return user
            with open('Tiktok_users.txt', 'w') as f:
                for i in range(users):
                    f.write(gnretorusers(let_user))
                    f.write("\n")
                    f.close
        file1 = open('Tiktok_users.txt', 'r')
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            # print(line.strip())
            usercheck = line.strip()
            checker = req.get(f"https://www.tiktok.com/@{usercheck}")
            if checker.status_code == 200:
                print(detect_color+"unavailable ==> " +
                      f"https://www.tiktok.com/@" + usercheck)
            else:
                print(green_color+"available ==> " +
                      f"https://www.tiktok.com/@" + usercheck)
        print("\n")
        print("\n")
        print(detect_color + "Message From Abu Layan")
        print(green_color + "Thanks For Useing My Script \n Bye")
    elif Q1 == "yes":
        UserfromClint = input(green_color+"Enter the username ==> ")
        print("\n")
        print("\n")
        checker2 = req.get(f"https://www.tiktok.com/@{UserfromClint}")
        if checker2.status_code == 200:
            print(detect_color+"unavailable ==> " +
                  f"https://www.tiktok.com/@" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
        else:
            print(green_color+"available ==> " +
                  f"https://www.tiktok.com/@" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
    else:
        print("You did not choose correct \n Bye")
elif Q == 3:
    Q1 = input(green_color+"You Want Search For Spcfivc User (yes/no) ==> ")
    print("\n")
    if Q1 == "no":
        print(banner_color+"Ex : Enter how many users you want ==>  100")
        print("\n")
        users = int(input(green_color + "Enter how many users you want ==> "))
        print("\n")
        print(banner_color+"Ex : Enter how many users you want ==>  3")
        let_user = int(
            input(green_color + "Enter how many letter user you want ==> "))
        print("\n")

        for i in range(users):
            def gnretorusers(let_user):
                user = ''
                letter = "qwertyuiopasdfghjklzxcvbnm"
                number = "1234567890"
                for i in range(let_user):
                    user += choice(letter + number)
                return user
            with open('users_twitter.txt', 'w') as f:
                for i in range(users):
                    f.write(gnretorusers(let_user))
                    f.write("\n")
                    f.close
        file1 = open('users_twitter.txt', 'r')
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            # print(line.strip())
            usercheck = line.strip()
            checker = req.get(f"https://www.tiktok.com/@{usercheck}")
            if checker.status_code == 200:
                print(detect_color+"unavailable ==> " +
                      f"https://twitter.com/" + usercheck)
            else:
                print(green_color+"available ==> " +
                      f"https://twitter.com/" + usercheck)
        print("\n")
        print("\n")
        print(detect_color + "Message From Abu Layan")
        print(green_color + "Thanks For Useing My Script \n Bye")
    elif Q1 == "yes":
        UserfromClint = input(green_color+"Enter the username ==> ")
        print("\n")
        print("\n")
        checker2 = req.get(f"https://twitter.com/{UserfromClint}")
        if checker2.status_code == 200:
            print(detect_color+"unavailable ==> " +
                  f"https://twitter.com/" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
        else:
            print(green_color+"available ==> " +
                  f"https://twitter.com/" + UserfromClint)
            print("\n")
            print("\n")
            print(detect_color + "Message From Abu Layan")
            print(green_color + "Thanks For Useing My Script \n Bye")
    else:
        print("You did not choose correct \n Bye")
