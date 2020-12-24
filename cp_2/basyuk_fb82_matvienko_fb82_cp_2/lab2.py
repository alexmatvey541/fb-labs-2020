abetka = ['а', 'б', 'в', 'г',  'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
n = 32

vibirka = {}
vibirka2 = {}

for i in range (len (abetka)):
    vibirka.update({abetka[i]:i})
    vibirka2.update({i:abetka[i]})
    
def decrypt (text, key):
    text = text.lower()
    key = key.lower()
    
    text1 = ''
    for i in text:
        if i in abetka:
            text1+=i

    text2 = ''
    for i in key:
        if i in abetka:
            text2+=i
    key = text2

    n1 = len(key)
    new_text = ''

    for i in range (len(text1)):
        new_text += vibirka2[(vibirka[text1[i]]-vibirka[key[i%n1]])%n]
    decrypted = new_text

    return(decrypted)

abetka=['а', 'б', 'в', 'г',  'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

LETTER_FREQUENCES = {'а': 0.0801, 'б': 0.0159, 'в': 0.0454, 'г': 0.017, 'д': 0.0298, 'е': 0.0849, 'ж': 0.0094, 'з': 0.0165,
                     'и': 0.0735,'й': 0.0121, 'к': 0.0349, 'л': 0.044, 'м': 0.0321, 'н': 0.067, 'о': 0.1097, 'п': 0.0281,
                     'р': 0.0473, 'с': 0.0547, 'т': 0.0626, 'у': 0.0262, 'ф': 0.0026, 'х': 0.0097, 'ц': 0.0048, 'ч': 0.0144,
                     'ш': 0.0073, 'щ': 0.0036,'ъ': 0.0004, 'ы': 0.019,'ь': 0.0174,'э': 0.0032, 'ю': 0.0064, 'я': 0.0201}

def found_key (len_of_key, text):

    len1 = len(text)
    real_key = ''

    for i in range (len_of_key): # розшифровуєм для підпослідовності її ключ

        the_text = ''
        dict3 = {}

        for k in range (i, len1, len_of_key):
            the_text+=text[k]

        for j in range (n):
            d_text = decrypt (the_text, abetka[j])
            d_len = len(d_text)
            d_len1 = 1/d_len

            dict1 = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0,
                   'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0,
                   'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0}

            for j2 in d_text:
                if j2 in dict1:
                    dict1[j2]+=1
                else:
                    pass

            xi2_index = 0
            
            for j3, j4 in dict1.items():
                xi2_index += ((LETTER_FREQUENCES[j3]*d_len1-j4)**2)/(LETTER_FREQUENCES[j3]*d_len1)

            dict3.update({j:xi2_index})
            
        min_value = (-1, float('inf'))

        for i5, j5 in dict3.items():
            if j5<min_value[1]:
                min_value=(i5, j5)
    
        real_key += abetka[min_value[0]]
    print(real_key)
    return (real_key)

def analyze_encrypted_text(text):
    len1 = len(text)
    dict2 = {}
    for i in range (2, 31):
        suma0 = 0
        
        for j in range (i):
            flag = 0
            dict1 = {}

            for k in range (j, len1, i):
                flag+=1

                if text[k] in dict1:
                    dict1[text[k]]+=1
                else:
                    dict1.update({text[k]: 1})
                    
            suma = 0
            
            for k1 in dict1.values():
                suma+=k1*(k1-1)
                
            suma0+=suma/((flag)*(flag-1))

        suma0/=i
        print("Індекс для тексту довжини ключа",i,": ", suma0)

        dict2.update({i:suma0})

    eps = 0.005
    rus_ind = 0.0553

    for i, j in dict2.items():
        if abs(j-rus_ind)<eps:
            value = int(i)
            print('довжина ключа:', value)

            found_key (value, text)
            proposed = decrypt (text, found_key (value, text))
    
            return proposed
    else:
        print('Неможливо встановити довжину ключа. Всі ключі відповідають рівномірному алфавіту!!!')
            
if __name__ == '__main__':

    text = input('Введіть текст:')

    print('Ваш текст: ', text)
    print(analyze_encrypted_text(text))

    KEYS = ['то', 'над', 'плащ', 'павук', 'абажур', 'підлога', 'пазушина', 'бібліотекарка']

    t_2 = decrypt (text, KEYS[0])
    print('Ключ з 2 літер (то): ', t_2)

    t_3 = decrypt (text, KEYS[1])
    print('Ключ з 3 літер (над): ', t_3)

    t_4 = decrypt (text, KEYS[2])
    print('Ключ з 4 літер (плащ): ', t_3)

    t_5 = decrypt (text, KEYS[3])
    print('Ключ з 5 літер (павук): ', t_5)

    t_6 = decrypt (text, KEYS[4])
    print('Ключ з 6 літер (абажур): ', t_6)

    t_7 = decrypt (text, KEYS[5])
    print('Ключ з 7 літер (підлога): ', t_7)

    t_8 = decrypt (text, KEYS[6])
    print('Ключ з 8 літер (пазушина): ', t_8)

    t_13 = decrypt (text, KEYS[7])
    print('Ключ з 13 літер (бібліотекарка): ', t_13)


    
