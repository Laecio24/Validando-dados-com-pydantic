from pydantic import BaseModel, Field, ValidationError

class Creature(BaseModel):
    name: str
    # Adicionando uma restrição de valor: max_length
    description: str = Field(max_length=20) 

print("--- Testando Erros de Validação ---")

# Erro 1: Erro de Tipo (passando lista em vez de string)
try:
    Creature(
        name="Hydra",
        country="GR",
        area="Lerna",
        description=["Muitas", "Cabeças"], # DEVERIA SER STR
        aka="Lernaean Hydra"
    )
except ValidationError as e:
    print("\nErro de Tipo detectado:")
    print(e.json())

# Erro 2: Erro de Valor (passando string maior que 20 caracteres)
try:
    Creature(
        name="Kraken",
        country="NO",
        area="Ocean",
        description="Um monstro gigante que afunda navios inteiros", # > 20 chars
        aka="Giant Squid"
    )
except ValidationError as e:
    print("\nErro de Valor detectado:")
    print(e.json())