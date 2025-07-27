def display_board(grid, reveal=False):
    print("  " + " ".join(str(i) for i in range(len(grid[0]))))
    for idx, row in enumerate(grid):
        line = []
        for cell in row:
            if cell == 'S' and not reveal:
                line.append('~')
            else:
                line.append(cell)
        print(f"{idx} " + " ".join(line))
