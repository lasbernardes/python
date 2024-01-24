# importado a biblioteca numpy
import numpy as np
print(np.__version__)

# Definindo a altura e a largura da imagem
height = 1000  # altura ou o número de linhas da imagem
width = 1000   # largura ou o número de colunas da imagem



# Implementar aqui
def geradorImagens(height=1280, width=720):
    random_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
    if random_image is None:
        return None

    return random_image
#enddef

#teste
random_image = geradorImagens()
#print('1> ',geradorImagens())
print('2> ',geradorImagens().shape) # deve retornar (1280, 720, 3)
print('3> ',geradorImagens(10).shape) # deve retornar (10, 720, 3)
print('4> ',geradorImagens(10,10).shape) # deve retornar (10, 10, 3)
print('5> ',geradorImagens(5,5)) # deve retornar uma matriz 5x5x3

print('-'*50)

#implementar aqui
def rgb2gray(random_image, f='NTSC'):
    if random_image is None:
        return None

    if f == 'NTSC':
        gray=[(0.299*random_image[:,:,0])+0.587*random_image[:,:,1]+0.114*random_image[:,:,2]]        
    elif f == 'media':
        gray=[(random_image[0]/3)+random_image[1]/3+random_image[2]/3]

    gray=np.array(gray, dtype=np.uint8)
    return gray



#%timeit (rgb2gray(random_image))
print((rgb2gray(random_image)))

print('-'*50)
'''
def rgb2gray1(random_image, f='NTSC'):
    gray=[]

    if random_image is None:
        return None

    if f == 'NTSC':
        for i in range(0,random_image.shape[0]):
            for j in range(0,random_image.shape[1]):
                gray[i][j]=0.299*random_image[0][i][j]+0.587*random_image[1][i][j]+0.114*random_image[2][i][j]
                
    elif f == 'media':
        for i in range(0,random_image.shape[0]):
            for j in range(0,random_image.shape[1]):
                gray[i,j]=(random_image[0,i,j]/3)+random_image[1,i,j]/3+random_image[2,i,j]/3

    gray=np.array(gray, dtype=np.uint8)
    return gray
'''


def rgb2gray1(random_image, f='NTSC'):
    if random_image is None:
        return None
    

    gray = np.zeros((random_image.shape[0], random_image.shape[1]), dtype=np.uint8)

    if f == 'NTSC':
        for i in range(random_image.shape[0]):
            for j in range(random_image.shape[1]):
                gray[i, j] = 0.299 * random_image[i, j, 0] + 0.587 * random_image[i, j, 1] + 0.114 * random_image[i, j, 2]

    elif f == 'media':
        for i in range(random_image.shape[0]):
            for j in range(random_image.shape[1]):
                gray[i, j] = (random_image[i, j, 0] / 3) + (random_image[i, j, 1] / 3) + (random_image[i, j, 2] / 3)

    return gray
#enddef


height=100
width =100
#random_image = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)
geradorImagens(height, width)
#%timeit (rgb2gray1(random_image))
print(rgb2gray1(random_image))

