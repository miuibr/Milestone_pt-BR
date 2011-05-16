Projeto de tradução da rom MIUI para Milestone para Português do Brasil.
==============================================================

Instruções para Windows
-----------------------

Copie o [*apktool.jar*](http://code.google.com/p/android-apktool/downloads/detail?name=apktool-1.3.1.tar.bz2&can=1&q=) para a pasta *./system/app/*.

### Descompilar ###

Para **descompilar** todos os arquivos de uma vez, crie um arquivo com nome *d_apk.bat* na  pasta *./system/app/*, copie o código do arquivo de mesmo nome existente na pasta *extras*, e salve-o.
Pronto, basta executá-lo.


Aplique os arquivos com a tradução, baixados do repositório.

### Compilar ###

Para compilar todos os arquivos de uma vez, crie um arquivo com nome *b_apk.bat* na  pasta *./system/app/*, copie o código do arquivo de mesmo nome existente na pasta *extras*, e salve-o.
Pronto, basta executá-lo.

Instruções para Mac OS X
-------------------------

Baixe o [*apktool.jar*](http://android-apktool.googlecode.com/files/apktool1.4.1.tar.bz2) e o 
[*aapt e apktool*](http://android-apktool.googlecode.com/files/apktool-install-macosx-r04-brut1.tar.bz2). Após isso,
copie todos os três para o diretório */usr/local/bin* com o seguinte comando:

`sudo cp aapt /usr/local/bin`

`sudo cp apktool.jar /usr/local/bin`

`sudo cp apktool /usr/local/bin`

### Descompilar ###

Para **descompilar** todos os apks que possuem tradução é só executar o script *copiar_apks.py* com o telefone conectado em modo debug
(para que adb poder se conectar a ele) usando o seguinte comando:

`python system/apps/copiar_apks.py`

Ele copiará todos os apks que possuem tradução (os que temos no repositório) do seu telefone, extrairá e juntará o pack pt-br com eles.

