import turtle as t # Turtle kütüphanesi t olarak adlandırıyoruz.
import random 

tim = t.Turtle() 
t.colormode(255) # Rgb olmasını isteidğimiz için
t.speed("fastest") # Hızlandırmak için

def random_color():
    r = random.randint(0, 255) # 0,255 aralığı rgb renk aralığıdır
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r , g , b)
    return  random_color 

#colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

directions = [0, 90, 180, 270] # her bir rakam pusuladaki değerlerle eşitir ve tim objemizin yani turtleımız'ın konumunu belirler sağa dön yukarı dön gibi.
tim.pensize(15) # tim objemizin yani Turtlımızın çizim yaparkenki çizgi büyüklüğü.

for _ in range(1200): # 1200 kez dönmesini istediğim için isteğe bağlı daha az veya fazla dönmesini sağlayabiliriz.
    tim.color(random_color()) # tim yani turtle'ın rengini belirliyoruz ama rastgele olmmasını istediğimiz için yukarıdaki random_color() olarak ayarlıyoruz.
    tim.forward(30) # Her bir renk'te 30 adım git gibi
    tim.setheading(random.choice(directions)) # pozisyonu'nu ayarlıyoruz rastgele olmasını istediğimiz için random.choice() kodu ile listeden rastgele konum/sayı çekiyoruz bu özelliğide random kütüphanesi sayesinde yapabiliyoruz.
