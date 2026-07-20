class city:
    def __init__(self,name,population):
        self.name=name
        self.population=population

c1=city("atp",20)
c2=city("kld",90)
c3=city("lo",8520) 

cities=[c1,c2,c3]
for city in cities:
    print(f"{city.name}id{city.population}")


# highest score in players    

class player:
    def __init__(self,name,score):
        self.name=name
        self.score=score

# creating instances through list and findinding who got highest score

p1=player("LOKI",85)
p2=player("SAI",45)
p3=player("LOHI",90)

players =[p1,p2,p3]
highest_score=0
highest_name=""
for player in players:
    if player.score>highest_score:
        highest_score=player.score
        highesst_name=player.name
        print(f"{player.name}and{player.score}")

