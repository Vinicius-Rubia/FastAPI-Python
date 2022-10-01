from fastapi import FastAPI

app = FastAPI()

shoppe = {
  1: {
    "item": "Fio Eletrico Cabo Flexivel 2,5mm 100 Metros.",
    "preco-unitario": 64.99,
    "quantidade": 1,
    "avaliacoes": "7,9mil",
    "vendido": "23,6mil",
    "estrelas": 4.8
  },
  2: {
    "item": "Bebedouro Gato Fonte Para Gatos Tipo Fonte",
    "preco-unitario": 39.99,
    "quantidade": 1,
    "avaliacoes": "5,2mil",
    "vendido": "10,1mil",
    "estrelas": 4.4
  },
  3: {
    "item": "Lovito Leggings Academia Esportivos Lipo Lisos de Secagem Rápida e Cintura Alta L09021 (Preto/Verde)",
    "preco-unitario": 36.90,
    "quantidade": 1,
    "avaliacoes": "6,8mil",
    "vendido": "13,4mil",
    "estrelas": 4.9
  },
  4: {
    "item": "Lovito Conjuntos Brasil Copa 2022 Esportivos Skinny de Alongamento Alto L13X090 (Verde/Cinza Claro/Rosa Claro)",
    "preco-unitario": 46.99,
    "quantidade": 1,
    "avaliacoes": "2,2mil",
    "vendido": "3,9mil",
    "estrelas": 4.6
  },
  5: {
    "item": "Torneira Gourmet de Cozinha Parede Metal Flexível 1/4 de Volta C-66",
    "preco-unitario": 51.99,
    "quantidade": 1,
    "avaliacoes": "1,8mil",
    "vendido": "3,4mil",
    "estrelas": 4.9
  },
  6: {
    "item": "Máquina De Cortar Cabelo Para Barba Masculina Designer Aleatório Elétrico Profissional",
    "preco-unitario": 39.90,
    "quantidade": 1,
    "avaliacoes": "22mil",
    "vendido": "43,2mil",
    "estrelas": 4.8
  },
  7: {
    "item": "Kit 10 Cuecas Boxer Box Microfibra Premium Mais Vendido",
    "preco-unitario": 49.99,
    "quantidade": 1,
    "avaliacoes": "2mil",
    "vendido": "3,7mil",
    "estrelas": 4.7
  },
  8: {
    "item": "Fone De Ouvido Sem Fio Pro 3 Tws Bluetooth Estéreo Com Pod Carregador",
    "preco-unitario": 61.80,
    "quantidade": 1,
    "avaliacoes": "9,4mil",
    "vendido": "24,8mil",
    "estrelas": 4.7
  },
  9: {
    "item": "Tapetes Peludos 1,50 X 1,00 Várias Cores Para Sala E Quarto",
    "preco-unitario": 49.90,
    "quantidade": 1,
    "avaliacoes": "36,3mil",
    "vendido": "73,3mil",
    "estrelas": 4.8
  },
  10: {
    "item": "Cortina de Voal Blackout 100% Corta Luz 2,20m x1,30m Cores Variadas",
    "preco-unitario": 52.30,
    "quantidade": 1,
    "avaliacoes": "4,8mil",
    "vendido": "9,7mil",
    "estrelas": 4.6
  },
}

@app.get("/")
def home():
  return {"Shoppe": shoppe}

@app.get("/produto/{id_produto}")
def pegar_venda(id_produto: int):
  return shoppe[id_produto]