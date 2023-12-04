from flag_gen import leet #install it by pip install flag_gen

user = input("[+] Enter text here: ")

unique = set() #Check if any charecter replicated. Onces found replication then it will store here. ZUL'S THEORY OK?!

for _ in range(0, 100): #The range is for how many time will it need to repeat. You can change the number if you want to have higher/lower flag possibility

    #We want the code to automate this plaintext string into a string that is unique. Maybe CTF may made this string possible.
    convert = leet(user)

    #Check if there's any replicated string. Previously we coded a Leet String. 
    #But we don't know if the script would replicate it back. 
    #So, this script will put all replicated charecter into the set to remove it, or reuse it for the enxt line of string.

    if convert not in unique:
        print(convert)
        unique.add(convert)


# Thanks for reading this script write-up. LOL
# If this happen again in a script where you need to get the flag using a pissbibility math,
# use this script to BRUTEFORCE THE FLAG!! MUAHAHAHAHAHAHAHAHAHA!
# OK OK I jokin, don't bruteforce the flag, please give mercy to the server. Don't stuff it like as if it's a giant vaccum
