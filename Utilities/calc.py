import click

req=raw_input('Enter two space seperated numbers: ')
a,b=map(float,req.split()) #two float numbers are stored in a and b

@click.command()
@click.option('--add',is_flag=True,help='Adds two numbers.')
@click.option('--sub',is_flag=True,help='Subtracts two numbers.')
@click.option('--mul',is_flag=True,help='Multiplies two numbers.')
@click.option('--div',is_flag=True,help='Divides two numbers.')
@click.option('--mod',is_flag=True,help='Takes modulus of two numbers.')

def cli(add,sub,mul, div, mod):
    	if(add): #for addition
    		print a+b
    	elif(sub): #for subtraction
    		print a-b
    	elif(mul): #for multiplication
    		print a*b
    	elif(div): #for division
    		print a/b
    	elif(mod): #for moulus
    		print a%b

