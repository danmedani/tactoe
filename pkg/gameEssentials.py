class GameEssentials:

  lines = []
  # Verts
  lines.append([[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]])
  lines.append([[0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 1, 3]])
  lines.append([[0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 2, 3]])
  lines.append([[0, 3, 0], [0, 3, 1], [0, 3, 2], [0, 3, 3]])
  lines.append([[1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3]])
  lines.append([[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3]])
  lines.append([[1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3]])
  lines.append([[1, 3, 0], [1, 3, 1], [1, 3, 2], [1, 3, 3]])
  lines.append([[2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 0, 3]])
  lines.append([[2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 1, 3]])
  lines.append([[2, 2, 0], [2, 2, 1], [2, 2, 2], [2, 2, 3]])
  lines.append([[2, 3, 0], [2, 3, 1], [2, 3, 2], [2, 3, 3]])
  lines.append([[3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3]])
  lines.append([[3, 1, 0], [3, 1, 1], [3, 1, 2], [3, 1, 3]])
  lines.append([[3, 2, 0], [3, 2, 1], [3, 2, 2], [3, 2, 3]])
  lines.append([[3, 3, 0], [3, 3, 1], [3, 3, 2], [3, 3, 3]])

  # Horizontals
  lines.append([[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]])
  lines.append([[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1]])
  lines.append([[0, 0, 2], [0, 1, 2], [0, 2, 2], [0, 3, 2]])
  lines.append([[0, 0, 3], [0, 1, 3], [0, 2, 3], [0, 3, 3]])
  lines.append([[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 3, 0]])
  lines.append([[1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1]])
  lines.append([[1, 0, 2], [1, 1, 2], [1, 2, 2], [1, 3, 2]])
  lines.append([[1, 0, 3], [1, 1, 3], [1, 2, 3], [1, 3, 3]])
  lines.append([[2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 3, 0]])
  lines.append([[2, 0, 1], [2, 1, 1], [2, 2, 1], [2, 3, 1]])
  lines.append([[2, 0, 2], [2, 1, 2], [2, 2, 2], [2, 3, 2]])
  lines.append([[2, 0, 3], [2, 1, 3], [2, 2, 3], [2, 3, 3]])
  lines.append([[3, 0, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]])
  lines.append([[3, 0, 1], [3, 1, 1], [3, 2, 1], [3, 3, 1]])
  lines.append([[3, 0, 2], [3, 1, 2], [3, 2, 2], [3, 3, 2]])
  lines.append([[3, 0, 3], [3, 1, 3], [3, 2, 3], [3, 3, 3]])

  # Other Horizontals
  lines.append([[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]])
  lines.append([[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1]])
  lines.append([[0, 0, 2], [1, 0, 2], [2, 0, 2], [3, 0, 2]])
  lines.append([[0, 0, 3], [1, 0, 3], [2, 0, 3], [3, 0, 3]])
  lines.append([[0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0]])
  lines.append([[0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1]])
  lines.append([[0, 1, 2], [1, 1, 2], [2, 1, 2], [3, 1, 2]])
  lines.append([[0, 1, 3], [1, 1, 3], [2, 1, 3], [3, 1, 3]])
  lines.append([[0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0]])
  lines.append([[0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1]])
  lines.append([[0, 2, 2], [1, 2, 2], [2, 2, 2], [3, 2, 2]])
  lines.append([[0, 2, 3], [1, 2, 3], [2, 2, 3], [3, 2, 3]])
  lines.append([[0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0]])
  lines.append([[0, 3, 1], [1, 3, 1], [2, 3, 1], [3, 3, 1]])
  lines.append([[0, 3, 2], [1, 3, 2], [2, 3, 2], [3, 3, 2]])
  lines.append([[0, 3, 3], [1, 3, 3], [2, 3, 3], [3, 3, 3]])

  # Flat Diags
  lines.append([[0, 0, 0], [1, 1, 0], [2, 2, 0], [3, 3, 0]])
  lines.append([[3, 0, 0], [2, 1, 0], [1, 2, 0], [0, 3, 0]])
  lines.append([[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1]])
  lines.append([[3, 0, 1], [2, 1, 1], [1, 2, 1], [0, 3, 1]])
  lines.append([[0, 0, 2], [1, 1, 2], [2, 2, 2], [3, 3, 2]])
  lines.append([[3, 0, 2], [2, 1, 2], [1, 2, 2], [0, 3, 2]])
  lines.append([[0, 0, 3], [1, 1, 3], [2, 2, 3], [3, 3, 3]])
  lines.append([[3, 0, 3], [2, 1, 3], [1, 2, 3], [0, 3, 3]])

  # Super Cross Diags
  lines.append([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
  lines.append([[3, 0, 0], [2, 1, 1], [1, 2, 2], [0, 3, 3]])
  lines.append([[0, 3, 0], [1, 2, 1], [2, 1, 2], [3, 0, 3]])
  lines.append([[3, 3, 0], [2, 2, 1], [1, 1, 2], [0, 0, 3]])

  # Normal Diags
  lines.append([[0, 0, 0], [0, 1, 1], [0, 2, 2], [0, 3, 3]])
  lines.append([[1, 0, 0], [1, 1, 1], [1, 2, 2], [1, 3, 3]])
  lines.append([[2, 0, 0], [2, 1, 1], [2, 2, 2], [2, 3, 3]])
  lines.append([[3, 0, 0], [3, 1, 1], [3, 2, 2], [3, 3, 3]])
  lines.append([[0, 0, 0], [1, 0, 1], [2, 0, 2], [3, 0, 3]])
  lines.append([[0, 1, 0], [1, 1, 1], [2, 1, 2], [3, 1, 3]])
  lines.append([[0, 2, 0], [1, 2, 1], [2, 2, 2], [3, 2, 3]])
  lines.append([[0, 3, 0], [1, 3, 1], [2, 3, 2], [3, 3, 3]])
  lines.append([[0, 3, 0], [0, 2, 1], [0, 1, 2], [0, 0, 3]])
  lines.append([[1, 3, 0], [1, 2, 1], [1, 1, 2], [1, 0, 3]])
  lines.append([[2, 3, 0], [2, 2, 1], [2, 1, 2], [2, 0, 3]])
  lines.append([[3, 3, 0], [3, 2, 1], [3, 1, 2], [3, 0, 3]])
  lines.append([[3, 0, 0], [2, 0, 1], [1, 0, 2], [0, 0, 3]])
  lines.append([[3, 1, 0], [2, 1, 1], [1, 1, 2], [0, 1, 3]])
  lines.append([[3, 2, 0], [2, 2, 1], [1, 2, 2], [0, 2, 3]])
  lines.append([[3, 3, 0], [2, 3, 1], [1, 3, 2], [0, 3, 3]])
