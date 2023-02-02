import random

guess_counter = 1

wanted_number = random.randint(1, 10)
print("Aklımdan 1 ile 10 arasında bir sayı tuttum. Tahmin etmeye çalış.")

guess = int(input("Tahminin:"))
while guess != wanted_number:
    if guess < wanted_number:
        print("Aklımda tuttuğum sayı bu sayıdan daha büyük.")
    else:
        print("Aklımda tuttuğum sayı bu sayıdan daha küçük.")

    guess = int(input("Tahminin:"))
    guess_counter += 1

print(f"Bildin! {guess_counter} kadar tahminde bildin.")
