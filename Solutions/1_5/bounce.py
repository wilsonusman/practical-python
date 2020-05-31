# bounce.py

height = 100
bounce = 1
while bounce <= 20:
    height = height * (3/5)
    print(bounce, round(height, 2))
    bounce += 1
