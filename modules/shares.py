from SR_71 import command
shares = command("net share")
shares = shares[2:-1]
print(shares)
for share in shares:
    print (share.split(' ', 1)[0])
    command("net share %s /DELETE" % share)