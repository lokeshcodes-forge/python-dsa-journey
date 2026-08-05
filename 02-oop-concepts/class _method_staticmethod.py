class car:
    total_carrs=0
    def __init__(self,model,year):
        self.model=model
        self.year=year
        car.total_carrs+=1
    @classmethod
    def get_total_carrs(cls):
        return cls.total_carrs
    @staticmethod
    def is_valid_year(year):
        return year<=2029



c1= car("swift",2022)
c2= car("i20",2024)
c3 = car("nexon",2027)


print(car.get_total_carrs())
print(car.is_valid_year(2030))
print(car.is_valid_year(2030))
