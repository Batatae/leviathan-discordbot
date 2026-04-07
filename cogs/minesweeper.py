from discord.ext import commands
import random

class minesweeper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.size = 5
        self.bombs_count = 10
        self.stts = False
        self.board = [["🌫️" for _ in range(self.size)] for _ in range(self.size)]
        self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.flags = []
        self.bombs = []
        self.numbers_reveal = {
                            0: "🟦",
                            1: "1️⃣",
                            2: "2️⃣",
                            3: "3️⃣",
                            4: "4️⃣",
                            5: "5️⃣",
                            6: "6️⃣",
                            7: "7️⃣",
                            8: "8️⃣"
                        }
        
    @commands.command(help="Para jogar digite !mines <dificuldade>. o bot gerará um campo minado de 5x5(default), e você terá que escolher as coordenadas para revelar as células. Caso haja uma bomba na célula escolhida, você perde. Para escolher uma célula, digite as coordenadas no formato !mines abrir <numero da linha> <numero da coluna> para revelar uma célula e !mines marcar <numero da linha> <numero da coluna> para colocar uma bandeira. Lembrando que o campo tera linhas e colunas numeradas de 1 a 5 e, ao abrir uma célula, o bot revelará o número de bombas adjacentes a ela. O objetivo é revelar todas as células sem bombas para vencer o jogo. Para desistir, digite !mines stop. dificuldades: facil = 10 bombas, 5x5. medio = 26 bombas, 8x8. dificil = 40 bombas, 10x10, hardcore = 90 bombas, 15x15.")

    

    
    async def mine(self, ctx, action: str = None, row: int = None, col: int = None):
        action = action.lower() if action else None

        dif = {
            "facil": (5, 10),
            "medio": (8, 26),
            "dificil": (10, 40),
            "hardcore": (15, 90)
        }

        if action is None or (action not in dif and action not in ["abrir", "marcar", "stop"]):
            await ctx.send("Ação inválida. Use !mines <dificuldade>, !mines abrir <linha> <coluna>, !mines marcar <linha> <coluna> ou !mines stop. :v")
            return
        
        
        
        if action in dif:
            if self.stts:
                await ctx.send("Um jogo já está em andamento. Use !mines stop para encerrar o jogo atual antes de iniciar um novo.")
                return
            
            self.size, self.bombs_count = dif[action]
            self.board = [["🌫️" for _ in range(self.size)] for _ in range(self.size)]
            self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
            self.flags = []
            self.bombs = []
            self.stts = True
            await ctx.send(f"Jogo iniciado! Use !mines abrir <linha> <coluna> para revelar uma célula e !mines marcar <linha> <coluna> para colocar uma bandeira. Lembre-se de que as linhas e colunas são numeradas de 1 a {self.size}. se quiser desistir, use !mines stop.\n\n{self.show_board()}")
            return

        if action == "stop":
            if not self.stts:
                await ctx.send("Nenhum jogo em andamento para encerrar. Use !mines start para iniciar um jogo.")
                return
            
            self.stts = False
            self.size = 5
            self.bombs_count = 10
            self.board = [["🌫️" for _ in range(self.size)] for _ in range(self.size)]
            self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
            self.flags = []
            self.bombs = []

            await ctx.send("Jogo encerrado. Se quiser jogar novamente, use !mines start. 🕊️")
            return
        
        if action in ["abrir", "marcar"]:
            if not self.stts:
                await ctx.send("Nenhum jogo em andamento. Use !mines start para iniciar um novo jogo. :v")
                return
            
            if row is None or col is None or not (1 <= row <= self.size and 1 <= col <= self.size):
                await ctx.send(f"Coordenadas inválidas. As linhas e colunas devem ser números entre 1 e {self.size}. Use !mines abrir <linha> <coluna> ou !mines marcar <linha> <coluna>. :v\n\n{self.show_board()}")
                return
               
            row -= 1
            col -= 1
            
            if action == "abrir":
                if not self.bombs:
                    self.board_gen(row, col)
                    

                if (row, col) in self.flags:
                    await ctx.send("Você não pode abrir uma célula marcada com uma bandeira. Use !mines marcar <linha> <coluna> para remover a bandeira antes de abrir a célula. :v\n\n{self.show_board()}")
                    return
                
                if (row, col) in self.bombs:
                    self.board[row][col] = "💣"
                    await ctx.send(f"💣💣💣💣 BOOOOOOMMMM!!!!\nVocê pisou numa bomba e teve seu corpo explodido em pedacinhos~\nPerdeu!\n\n{self.show_board()}")
                    self.stts = False
                    self.size = 5
                    self.bombs_count = 10
                    self.board = [["🌫️" for _ in range(self.size)] for _ in range(self.size)]
                    self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
                    self.flags = []
                    self.bombs = []
                    return
                
                if self.board[row][col] != "🌫️":
                    await ctx.send(f"Essa célula já foi revelada. Escolha outra célula para abrir. :v\n\n{self.show_board()}")
                    return

                self.board_reveal(row,col)

                safe_cells = self.size * self.size - len(self.bombs)
                revealed = sum(
                    1 for i in range(self.size) for j in range(self.size)
                    if self.board[i][j] != "🌫️" and self.board[i][j] != "🚩"
                )

                if revealed == safe_cells:
                    await ctx.send(f"Parabéns! Você revelou todas as células sem bombas e venceu o jogo! 🎉\n\n{self.show_board()}")
                    self.stts = False
                    self.size = 5
                    self.bombs_count = 10
                    self.board = [["🌫️" for _ in range(self.size)] for _ in range(self.size)]
                    self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
                    self.flags = []
                    self.bombs = []
                    return
                
                await ctx.send(f"Célula revelada!\n\n{self.show_board()}\nContinua ai, só toma cuidado...")
                return
            
            if action == "marcar":
                if (row, col) in self.flags:
                    self.flags.remove((row, col))
                    self.board[row][col] = "🌫️"
                    await ctx.send(f"Bandeira removida!\n\n{self.show_board()}")
                    return
                
                if self.board[row][col] != "🌫️":
                    await ctx.send(f"Essa célula já foi revelada. Você não pode colocar uma bandeira nela. Escolha outra célula para marcar ou abrir.\n\n{self.show_board()}")
                    return
                
                if len(self.flags) >= self.bombs_count:
                    await ctx.send(f"Você já colocou o número máximo de bandeiras ({self.bombs_count}). Remova uma bandeira existente para colocar uma nova.\n\n{self.show_board()}")
                    return
                
                self.flags.append((row, col))
                self.board[row][col] = "🚩"
                await ctx.send(f"Bandeira colocada!\n\n{self.show_board()}\nContinue abrindo com cuidado!")
        
        else:
            await ctx.send("Ação inválida. Use !mines start, !mines abrir <linha> <coluna>, !mines marcar <linha> <coluna> ou !mines stop. :v")
            return


    def show_board(self):
        return "\n".join("".join(str(celula) for celula in linha) for linha in self.board)

    def board_gen(self, first_row, first_col):
            self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
            self.bombs = []
            
            while len(self.bombs) < self.bombs_count:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)

                if (row, col) not in self.bombs and (row, col) != (first_row, first_col):
                    if abs(row - first_row) <= 1 and abs(col - first_col) <= 1:
                        continue
                    self.bombs.append((row, col))
                    self.cells[row][col] = -1

                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = row + dr, col + dc

                            if dr == 0 and dc == 0:
                                continue

                            if 0 <= nr < self.size and 0 <= nc < self.size and self.cells[nr][nc] != -1:
                                self.cells[nr][nc] += 1
            print(self.bombs)

    def board_reveal(self, row, col):
        

        if self.cells[row][col] == 0:
            self.board[row][col] = self.numbers_reveal[0]
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc

                    if dr == 0 and dc == 0:
                        continue

                    if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == "🌫️":
                        self.board_reveal(nr, nc)
        
        else:
            self.board[row][col] = self.numbers_reveal[self.cells[row][col]]
            return

async def setup(bot):
    await bot.add_cog(minesweeper(bot))
