DATA = [
  { "t": "A", "notas": [3,4,5,6,7], "mx": 5 },
  { "t": "B", "notas": [1,3,5,7,9], "mx": 5 },
  { "t": "C", "notas": [5,5,5,5,5], "mx": 5 },
  { "t": "D", "notas": [3,5,5,6,6], "mx": 5 }
]

def main():
  soma = 0

  for sala in DATA:
    notas = sala["notas"]
    mx = sala["mx"]

    for nota in notas:
      soma += (nota - mx) ** 2

    media_g = soma /  mx

    print(f"{sala["t"]}: `{media_g}`")

if __name__ == "__main__":
  main()
