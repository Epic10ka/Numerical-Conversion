               #Funções
                                                   #Binário
def pt_decbin():
    num = int(input('Digite o número: '))
    print(f'O número em binário é : {bin(num)[2:]}')

def en_decbin():
    num = int(input('Enter the number: '))
    print(f'The binary number is: {bin(num)[2:]}')

def pt_bindec():
    binary = input('Digite o número binário: ')
    dec = int(binary, 2)
    print(f'O número em decimal é {dec}')

def en_bindec():
    binary = input('Enter the binary number: ')
    dec = int(binary, 2)
    print(f'The binary number is: {dec}')

def pt_hexbin():
    hexa = input('Digite o número hexadecimal: ')
    hexbin = int(hexa, 16)
    binary = bin(hexbin)[2:]
    print(f'O número em binário é {binary}')

def en_hexbin():
    hexa = input('Enter the hexadecimal number: ')
    hexbin = int(hexa, 16)
    binary = bin(hexbin)[2:]
    print(f'The hexadecimal number is {binary}')

def pt_binhexa():
    binary = input('Digite o número binário: ')
    binhex = int(binary, 2)
    hexa = hex(binhex)[2:]
    print(f'O número em hexadecimal é {hexa.upper()}')

def en_binhexa():
    binary = input('Enter the binary number: ')
    binhex = int(binary, 2)
    hexa = hex(binhex)[2:]
    print(f'The hexadecimal number is {hexa.upper()}')
                                                  #Binário


                                                  #Hexadecimal
def pt_dechexa():
    num = int(input('Digite o número: '))
    print(f'O número em hexadecimal é: {hex(num).upper()[2:]}')

def en_dechexa():
    num = int(input('Enter the number: '))
    print(f'The hexadecimal number is: {hex(num).upper()[2:]}')

def pt_hexdec():
    hexa = input('Digite o número hexadecimal: ')
    dec = int(hexa, 16)
    print(f'O númer em decimal é: {dec}')

def en_hexdec():
    hexa = input('Enter the number: ')
    dec = int(hexa, 16)
    print(f'The decimal number is {dec}')
                                                #Hexadecimal


                                                 #Octal
def pt_decoct():
    num = int(input('Digite o número: '))
    print(f'O número em octal é {oct(num)[2:]}')

def en_decoct():
    num = int(input('Enter the number: '))
    print(f'The octal number is {oct(num)[2:]}')

def pt_octdec():
    octa = input('Digite o número octal: ')
    dec = int(octa, 8)
    print(f'O número em decimal é {dec}')

def en_octdec():
    octa = input('Enter the octal number: ')
    dec = int(octa, 8)
    print(f'The decimal number is {dec}')

def pt_binoct():
    binary = input('Digite o número binário: ')
    dec = int(binary, 2)
    print(f'O número em octal é {oct(dec)[2:]}')

def en_binoct():
    binary = input('Enter the binary number:: ')
    dec = int(binary, 2)
    print(f'The octal number is {oct(dec)[2:]}')

def pt_octbin():
    octa = input('Digite o número octal: ')
    dec = int(octa, 8)
    binary = bin(dec)
    print(f'O número em binário é {binary[2:]}')
def en_octbin():
    octa = input('Enter the octal number: ')
    dec = int(octa, 8)
    binary = bin(dec)
    print(f'The binary number is {binary[2:]}')

def pt_octhexa():
    octa = input('Digite o número octal: ')
    dec = int(octa, 8)
    hexa = hex(dec)
    print(f'O número em hexadecimal é {hexa.upper()[2:]}')

def en_octhexa():
    octa = input('Enter the octal number: ')
    dec = int(octa, 8)
    hexa = hex(dec)
    print(f'The hexadecimal number is {hexa.upper()[2:]}')

def pt_hexaoct():
    hexa = input('Digite o número hexadecimal: ')
    dec = int(hexa, 16)
    octa = oct(dec)
    print(f'O número em octal é {octa[2:]}')

def en_hexaoct():
    hexa = input('Enter the exadecimal number: ')
    dec = int(hexa, 16)
    octa = oct(dec)
    print(f'The octal number is {octa[2:]}')
                                           #Octal
#FIM DAS FUNÇÕES

                               #Aparência
from time import sleep
from colorama import init, Fore, Style
init()

print()
print('\033[1m|Language selection|\033[m'.center(35))
print('\033[1;92mPORTUGUESE\033[m \033[1m(1)\033[m or \033[1;34mENGLISH\033[m \033[1m(2)\033[m'.center(10))
print()
language = input('Select your language: ').upper()

if language == '1' or language.startswith ('P'):
    print()
    print('Connecting...')
    sleep(1)
    print()
    print('                       =—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=')
    print(Fore.MAGENTA + 'CONVERSÃO DE NÚMEROS'.center(90) + Style.RESET_ALL)
    print('                       =—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=')
    print()
    print('\033[4;97m|OPÇÕES|\033[m'.center(95))
    print('\033[1mDECIMAL, BINÁRIO, HEXADECIMAL e OCTAL\033[m'.center(92))
    print()

    from_input = input('                        Converter de: ').upper()
    to_input =  input('                        Para: ').upper()
    if from_input.startswith('DEC') and to_input.startswith('BIN'):
        print()
        pt_decbin()
    elif from_input.startswith('DEC') and to_input.startswith('HEX'):
        print()
        pt_dechexa()
    elif from_input.startswith('DEC') and to_input.startswith('OCT'):
        print()
        pt_decoct()
    elif from_input.startswith('BIN') and to_input.startswith('DEC'):
        print()
        pt_bindec()
    elif from_input.startswith('BIN') and to_input.startswith('HEX'):
        print()
        pt_binhexa()
    elif from_input.startswith('BIN') and to_input.startswith('OCT'):
        print()
        pt_binoct()
    elif from_input.startswith('HEX') and to_input.startswith('DEC'):
        print()
        pt_hexdec()
    elif from_input.startswith('HEX') and to_input.startswith('BIN'):
        print()
        pt_hexbin()
    elif from_input.startswith('HEX') and to_input.startswith('OCT'):
        print()
        pt_hexaoct()
    elif from_input.startswith('OCT') and to_input.startswith('DEC'):
        print()
        pt_octdec()
    elif from_input.startswith('OCT') and to_input.startswith('BIN'):
        print()
        pt_octbin()
    elif from_input.startswith('OCT') and to_input.startswith('HEX'):
        print()
        pt_octhexa()

    elif language == '2' or language.startswith ('E'):
        print()
        print('Connecting...')
        sleep(1)
        print()
        print('                       =—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=')
        print(Fore.MAGENTA + 'NUMBERS CONVERSION'.center(90) + Style.RESET_ALL)
        print('                       =—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=—=')