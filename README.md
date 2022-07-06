# Extrator de texto de Imagens
O projeto consiste em uma sistema em flask para extração de texto em Imagens.
Para utilizar o sistema primeiro é necessário instalar o Tesseract a partir das instrulções do link <a href="https://github.com/UB-Mannheim/tesseract/wiki">https://github.com/UB-Mannheim/tesseract/wiki</a>
e as dependencias do projeto com os comandos
```
pip install -r requirements.txt
```
e então executar o projeto com o comando:
```
python app.py
```

A seguir vemos a tela inicial do projeto:
<img src="https://raw.githubusercontent.com/Sheliga/images/master/projects/flask_ocr/extrair_texto_imagem.jpg"/>

para utilizar basta selecionar o arquivo no botão "selecionar arquivo" e então clicar no upload, o texto irá aparecer na area de texto no fim da pagina,
para testar o projeto recomendo o uso do arquivo "teste.jpg" que se encontra na pasta upload
