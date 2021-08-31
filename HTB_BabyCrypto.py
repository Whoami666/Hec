ct = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
ctbytes = bytes.fromhex(ct)
print(ctbytes)

decr = ""
for i in range(len(ctbytes)):
    print(ctbytes[i])
    x = ctbytes[i]
    if x < 18:
        x += 256
    x -= 18
    while x % 123 > 0:
        x += 256
    decr += chr(x // 123)
print(decr)