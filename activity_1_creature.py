from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

dict_thing = {
    "name": "yeti",
    "country": "CN",
    "area": "Himalayas",
    "description": "Hirsute Himalayan",
    "aka": "Abominable Snowman",
}

# 3. Instanciando objetos
# Usando o dicionário original com desempacotamento (**)
c1 = Creature(**dict_thing)

# Criaturas inventadas
c2 = Creature(
    name="Chupacabra", 
    country="PR", 
    area="Farm", 
    description="Goat sucker", 
    aka="El Chupacabra"
)
c3 = Creature(
    name="Curupira", 
    country="BR", 
    area="Amazon Forest", 
    description="Feet turned backwards", 
    aka="Forest Protector"
)

# 4. Imprimir nomes
creatures = [c1, c2, c3]
for c in creatures:
    print(f"Creature Name: {c.name}")