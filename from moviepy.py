from moviepy.editor import vfx, VideoFileClip, concatenate_videoclips

video01 = VideoFileClip("videoteste.mp4").subclip(0, 10).fx(vfx.fadeout, 2) 
video02 = VideoFileClip("videoteste.mp4").subclip(20, 30).fx(vfx.fadeout, 2)

edicaofinal = concatenate_videoclips([video01, video02])
edicaofinal.write_videfile("VideoPronto.mp4")

#Como o código acima funciona ?

#VideoFileClip("videoteste.mp4") Seleciona o video a ser editado

#subclip(0, 10) os valores dentro dos parenteses são o tempo do video

#Nesse caso ele esta pegando o video desde o inicio "0" e cortando nos 10 segundos 

#.fx() aplica um efeito no video, nesse caso utilizei o vfx.fadeout e o valor dentro dos parentes é o tempo do efeito

#na linha abaixo recortei um outro video

#concatenate_videoclips([video01, video02]) junta os dois videos 

#.write_videfile("VideoPronto.mp4") renderiza o video em formato mp4