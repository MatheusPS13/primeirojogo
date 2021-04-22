from PIL import Image

def ajusta_imagem(pasta,arq,out,height,ang,flip):
    img = Image.open(pasta_imagens + arq)
    (w, h) = img.size

    hpercent = (height / float(h))
    wsize = int((float(w) * float(hpercent)))

    img = img.resize((wsize, height), Image.ANTIALIAS)
    if not ang==0:
        img = img.rotate(ang)

    if flip > 0:
        img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    elif flip < 0:
        img = img.transpose(method=Image.FLIP_TOP_BOTTOM)

    img.save(pasta_imagens + out)


pasta_imagens = '..\Jogo_Cobrinha\Imagens\ '
pasta_imagens = pasta_imagens[:-1]

(width,height) = (600,600)

arq = 'green-grass-textures.jpg'
out = 'fundo.png'
ajusta_imagem(pasta_imagens,arq,out,height,0,0)

arq = 'cabeça_cobra.png'
out = 'cabeca_d.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),0,0)
out = 'cabeca_e.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),180,0)
out = 'cabeca_c.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),90,0)
out = 'cabeca_b.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),-90,0)
out = 'cabeca_df.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),0,-1)
out = 'cabeca_ef.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),180,-1)
out = 'cabeca_cf.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),90,1)
out = 'cabeca_bf.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.05*height),-90,1)

arq = 'apple.png'
out = 'alimento.png'
ajusta_imagem(pasta_imagens,arq,out,int(0.06*height),0,0)

