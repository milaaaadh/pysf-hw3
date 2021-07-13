def photographic_encryption(user_text, user_size):
    import turtle

    alphabet_color = {}
    alphabet_with_space = ' abcdefghijklmnopqrstuvwxyz'
    colors = ('black', 'gray', 'silver', 'whitesmoke', 'rosybrown', 'firebrick', 'red', 'darksalmon', 'sienna',
              'sandybrown', 'bisque', 'tan', 'moccasin', 'floralwhite', 'gold', 'darkkhaki', '#FAFAD2',
              'olivedrab', 'chartreuse', '#598556', 'lightgreen', 'green', 'mediumseagreen', 'mediumaquamarine',
              'mediumturquoise', 'darkslategray', 'blue')
    # FAFAD2 is Light Goldenrod Yellow
    # 598556 is dark sage
    for i in range(27):
        alphabet_color[alphabet_with_space[i]]=colors[i]

    print(alphabet_color)
    def make_square ( size , color ) :
        a.speed ( 300 )
        a.fillcolor ( color )
        a.begin_fill ( )
        a.forward ( size )
        a.left ( 90 )
        a.forward ( size )
        a.left ( 90 )
        a.forward ( size )
        a.left ( 90 )
        a.forward ( size )
        a.left ( 90 )
        a.forward ( size )
        a.end_fill ( )


    count = 1
    x = 0
    a = turtle.Turtle ( )

    for alphabet in user_text:
        fill_color = alphabet_color[alphabet]
        y , x = x , (count - 1) // 14

        if x == y:
            make_square(user_size,fill_color)
        else:
            a.goto(0,-user_size*x)
            make_square(user_size, fill_color)
        count = count + 1
    turtle.done ( )


def pigpen_encryptor ( text ) :
    pigpen_chars = [ 'ᒧ' , '⊔' , 'ᒪ' , '⊐' , '□' , '⊏' , 'ᒣ' , '⊓' , 'ᒥ' , 'ᒧx' , '⊔x' , 'ᒪx' , '⊐x' , '□x' , '⊏x' ,
                     'ᒣx' , '⊓x' , 'ᒥx' , 'ᒧo' , '⊔o' , 'ᒪo' , '⊐o' , '□o' , '⊏o' , 'ᒣo' , '⊓o' ]
    pigpen_dict = { }
    reverse_pigpen_dict = { }
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range ( 26 ) :
        pigpen_dict [ pigpen_chars [ i ] ] = alphabet [ i ]
        reverse_pigpen_dict [ alphabet [ i ] ] = pigpen_chars [ i ]

    encrypt = ''
    for z in text :
        if z in alphabet :
            encrypt = encrypt + reverse_pigpen_dict [ z ]
        else :
            encrypt = encrypt + z
    return (encrypt)


def pigpen_decryptor ( text ) :
    pigpen_chars = [ 'ᒧ' , '⊔' , 'ᒪ' , '⊐' , '□' , '⊏' , 'ᒣ' , '⊓' , 'ᒥ' , 'ᒧx' , '⊔x' , 'ᒪx' , '⊐x' , '□x' , '⊏x' ,
                     'ᒣx' , '⊓x' , 'ᒥx' , 'ᒧo' , '⊔o' , 'ᒪo' , '⊐o' , '□o' , '⊏o' , 'ᒣo' , '⊓o' ]
    pigpen_dict = { }
    reverse_pigpen_dict = { }
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range ( 26 ) :
        pigpen_dict [ pigpen_chars [ i ] ] = alphabet [ i ]
        reverse_pigpen_dict [ alphabet [ i ] ] = pigpen_chars [ i ]

    decrypt = ''
    i = 0
    for z in text :
        if i < len ( text ) - 1 :
            i = i + 1
        if z == 'o' or z == 'x' :
            continue
        elif z in pigpen_chars :
            if text [ i ] == 'o' or text [ i ] == 'x' :
                z = z + text [ i ]
            decrypt = decrypt + pigpen_dict [ z ]
        else :
            decrypt = decrypt + z

    return (decrypt)


def caesar_encryptor ( text , number ) :
    number = number % 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = { }
    reverse_alphabet_dict = { }

    i = 0
    for j in alphabet :
        alphabet_dict [ j ] = i
        reverse_alphabet_dict [ i ] = j
        i = i + 1

    encrypt = ''
    for z in text :
        if z in alphabet_dict :
            a = 0
            a = alphabet_dict [ z ] + number
            if a > 25 :
                a = a - 26
            encrypt = encrypt + reverse_alphabet_dict [ a ]
        else :
            encrypt = encrypt + z

    return encrypt


def caesar_decryptor ( text , number ) :
    number = number % 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = { }
    reverse_alphabet_dict = { }

    i = 0
    for j in alphabet :
        alphabet_dict [ j ] = i
        reverse_alphabet_dict [ i ] = j
        i = i + 1

    decrypt = ''
    for z in text :
        if z in alphabet_dict :
            a = 0
            a = alphabet_dict [ z ] - number
            if a < 0 :
                a = a + 26
            decrypt = decrypt + reverse_alphabet_dict [ a ]
        else :
            decrypt = decrypt + z

    return decrypt


user_method = input ( "Please select your cypher type (1- Caesar cipher , 2 – Pig Pen, 3- photographic_encryption :   " )
operation = input ( "Enter you operation ( 1-encrypt , 2-decrypt):   " )
# if user_method.lower() == "Pig Pen" or user_method.lower() == "2":
# print("If need pigpen characters see this link")
# time.sleep(5)
# webbrowser.open('https://www.programmersought.com/article/57652656603/')
user_text = input ( "enter your message:   " )

if user_method.lower ( ) == "caesar cipher" or user_method.lower ( ) == "1" :
    if operation.lower ( ) == "encrypt" or operation.lower ( ) == "1" :
        user_number = int ( input ( "enter your encrypt number:   " ) )
        final_message = caesar_encryptor ( user_text , int ( user_number ) )
        print ( final_message )
    elif operation.lower ( ) == "decrypt" or operation.lower ( ) == "2" :
        user_number = int ( input ( "enter your decrypt number:   " ) )
        final_message = caesar_decryptor ( user_text , int ( user_number ) )
        print ( final_message )

elif user_method.lower ( ) == "Pig Pen" or user_method == "2" :
    if operation.lower ( ) == "encrypt" or operation.lower ( ) == "1" :
        final_message = pigpen_encryptor ( user_text )
        print ( final_message )
    elif operation.lower ( ) == "decrypt" or operation.lower ( ) == "2" :
        final_message = pigpen_decryptor ( user_text )
        print ( final_message )
elif user_method.lower() == "photographic_encryption" or user_method == "3":
    user_size = int(input("please enter your square size: "))
    photographic_encryption(user_text,user_size)