from PIL import Image

def ajusta_imagem(pasta,arq,out,height):
    img = Image.open(pasta_imagens + arq)
    (w, h) = img.size

    hpercent = (height / float(h))
    wsize = int((float(w) * float(hpercent)))

    img = img.resize((wsize, height), Image.ANTIALIAS)

    img.save(pasta_imagens + out)


pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

(width,height) = (600,600)

arq = 'green-grass-textures.jpg'
out = 'fundo.png'
ajusta_imagem(pasta_imagens,arq,out,height)

arq = 'cabeça_cobra.png'
out = 'cabeca.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height))

