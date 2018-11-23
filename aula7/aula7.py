import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """

    t.begin_fill()         # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line

def per_resp (pergunta):
    print (pergunta)
    resposta = input() 
    return resposta

cor_panel = per_resp('What is the color of the panel?')

def per_resp2 (per1,per2):
	print (per1,per2)
	resp1 = input(per1)
	resp2 = input(per2)
	resposta1 = (resp1,resp2)	
	return resposta1 

	 
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor(cor_panel)

cor_tess = per_resp2('What is the color of the turtle? ', 'What is the color of the gap? ' )

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color(cor_tess[0],cor_tess[1])
tess.pensize(3)
	
def funcao_xs (dados):
	lista = dados.split()
	return lista

xs = funcao_xs(input())

for a in xs:
    draw_bar(tess, int(a)) 

#wn.mainloop()
