import sys
patterns = {
    "0": [" -- ", "|  |", "|  |", "    ", "|  |", "|  |", " -- "],
    "1": ["    ", "   |", "   |", "    ", "   |", "   |", "    "],
    "2": [" -- ", "   |", "   |", " -- ", "|   ", "|   ", " -- "],
    "3": [" -- ", "   |", "   |", " -- ", "   |", "   |", " -- "],
    "4": ["    ", "|  |", "|  |", " -- ", "   |", "   |", "    "],
    "5": [" -- ", "|   ", "|   ", " -- ", "   |", "   |", " -- "],
    "6": [" -- ", "|   ", "|   ", " -- ", "|  |", "|  |", " -- "],
    "7": [" -- ", "   |", "   |", "    ", "   |", "   |", "    "],
    "8": [" -- ", "|  |", "|  |", " -- ", "|  |", "|  |", " -- "],
    "9": [" -- ", "|  |", "|  |", " -- ", "   |", "   |", " -- "],
}

while True:
  try:
    line = input()
    if not line:
      continue
    s = line.strip()
    width = len(s) * 4 + (len(s) - 1)
    print("x" + "-" * width + "x")
    for i in range(7):
      row_pieces = []
      for digit in s:
        if digit in patterns:
          row_pieces.append(patterns[digit][i])
        else:
          row_pieces.append("    ")

      new_var = print("|" + " ".join(row_pieces) + "|")
      new_var
      print("x" + "-" * width + "x")

  except EOFError:
    break