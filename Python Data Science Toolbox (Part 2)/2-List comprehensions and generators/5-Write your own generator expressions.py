# Generatörlerde elinizde iterasyona tabi tutacağınız elemanlar halihazırda mevcut değildir, siz
# bir sonrakini çağırdığınız zaman üretilir ve size sunulur. Bu ne işimize yarayacak derseniz,
# yapacağınız işlem için bir listenin tüm elemanlarına ihtiyacınız yoksa veya ne kadarını kullanacağınızı
# bilmiyorsanız boşu boşuna listenin hepsini oluşturup memory’yi şişirmek yerine generatör kullanarak ihtiyaç
# duydukça/çağırdıkça elemanların üretilmesini sağlayıp fazla memory kullanımının önüne geçebilirsiniz.

# generator object does not create the entire list

result = (num for num in range(0,31))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for num in result:
    print(num)
