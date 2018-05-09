# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:49:28 2018

@author: adityanalge
"""

#Global Variables

a=b=c=d=e=f=g=h=i=' '
count = 0
play = 1
mylist=[]
replay = True
#Asking Players to Choose 'X' or 'O'

while replay:

	while True:
		print ("\nWelcome to Tic Tac Toe!")
		print ("\nPlayer 1: Do You Want To Play X or O?")
		player1 = input().upper()
		if player1 == 'X' or 'O':
			break
		else:
			print('\nInvalid Input! Enter X or O.')

	#'X' plays first and 'O' plays second
	if player1 == 'X':
		print('\nPlayer 1 will go first.')
		print('-------------------------------------------------')
		player2 = 'O'
	elif player2 == 'O':
		print('\nPlayer 2 will go first.')
		print('-------------------------------------------------')
		player2 ='X'

	#Waiting for players to get ready to play
	while True:
		print('\nAre you ready to play? Enter Yes or No.')
		ready = input().lower()
		if ready == 'yes':
			break
		elif ready == 'no':
			print('\nStart When Ready!')
		else:
			print('\nInvalid Input! Enter Yes or No.')

	#Main logic of program inside a while loop
	while ready=='yes':

		while True:
			print('')
			print('Choose your position:(1-9)') 
			j = int(input())
			if j not in mylist:
				mylist.append(j)
				print('')
				count+=1
				break
			else:
				print("Position Already Marked. Please choose another position")
	        
		if play == 1 and j==7:
		    a = 'X'
		    play = 2
		elif play == 2 and j == 7:
		    a = 'O'
		    play = 1
		if play == 1 and j==8:
		    b = 'X'
		    play = 2
		elif play == 2 and j == 8:
		    b = 'O'
		    play = 1 
		if play == 1 and j==9:
		    c = 'X'
		    play = 2
		elif play == 2 and j == 9:
		    c = 'O'
		    play = 1
		if play == 1 and j==4:
		    d = 'X'
		    play = 2
		elif play == 2 and j == 4:
		    d = 'O'
		    play = 1
		if play == 1 and j==5:
		    e = 'X'
		    play = 2
		elif play == 2 and j == 5:
		    e = 'O'
		    play = 1
		if play == 1 and j==6:
		    f = 'X'
		    play = 2
		elif play == 2 and j == 6:
		    f = 'O'
		    play = 1
		if play == 1 and j==1:
		    g = 'X'
		    play = 2
		elif play == 2 and j == 1:
		    g = 'O'
		    play = 1
		if play == 1 and j==2:
		    h = 'X'
		    play = 2
		elif play == 2 and j == 2:
		    h = 'O'
		    play = 1
		if play == 1 and j==3:
		    i = 'X'
		    play = 2
		elif play == 2 and j == 3:
		    i= 'O'
		    play = 1

		print('    |    |    ')
		print(' {}  | {}  | {} '.format(a,b,c))
		print('    |    |    ')
		print('--------------')
		print('    |    |    ')
		print(' {}  | {}  | {} '.format(d,e,f))
		print('    |    |    ')
		print('--------------')
		print('    |    |    ')
		print(' {}  | {}  | {} '.format(g,h,i))
		print('    |    |    ')
		print('\n')

		if a==b==c=='X':
	    	print("Congratulations! Player 1 Wins.")
	    	break
		elif a==b==c=='O':
	    	print("Congratulations! Player 2 Wins.")
	    	break
		if d==e==f=='X':
	    	print("Congratulations! Player 1 Wins.")
	    	break
		elif d==e==f=='O':
	    	print("Congratulations! Player 2 Wins.")
	    	break
		if g==h==i=='X':
	    	print("Congratulations! Player 1 Wins.")
	    	break
		elif g==h==i=='O':
	    	print("Congratulations! Player 2 Wins.")
	    	break
		if a==d==g=='X':
	    	print("Congratulations! Player 1 Wins.")
	    	break
		elif a==d==g=='O':
	    	print("Congratulations! Player 2 Wins.")
	    	break
		if b==e==h=='X':
		    print("Congratulations! Player 1 Wins.")
		    break
		elif b==e==h=='O':
		    print("Congratulations! Player 2 Wins.")
		    break
		if c==f==i=='X':
		    print("Congratulations! Player 1 Wins.")
		    break
		elif c==f==i=='O':
		    print("Congratulations! Player 2 Wins.")
		    break
		if a==e==i=='X':
		    print("Congratulations! Player 1 Wins.")
		    break
		elif a==e==i=='O':
		    print("Congratulations! Player 2 Wins.")
		    break
		if c==e==g=='X':
		    print("Congratulations! Player 1 Wins.")
		    break
		elif c==e==g=='O':
		    print("Congratulations! Player 2 Wins.")
		    break    
		if count == 9:
		    print("\nIt's a Draw!")
		    break
		
		print('-------------------------------------------------')
		print('Do You Want to Play Again? Enter Yes or No')
		inp = input().lower()
		if ready == 'yes':
		    pass
		elif ready == 'no':
		    print('\nGoodbye')
		    break
		else:
		    print('\nInvalid Input! Enter Yes or No.')