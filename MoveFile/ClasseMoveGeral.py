"""
Script que permite organizar um diretório, movendo os arquivos de acordo com a sua extensão para suas respectivas
pastas. Esse script simples e meio bagunçado foi feito para atender às minhas necessidades e podendo sempre melhorar.
Sinta-se à vontade para efetuar melhorias.
"""

import os
import shutil


class MoveFile:
    srcdir = input('Informe a pasta de origem: ')

    def __init__(self,
                 filezip=srcdir + r'\Arquivos_zip', filepdf=srcdir + r'\PDF',
                 filetxt=srcdir + r'\TXT',
                 filexlsx=srcdir + r'\Excel', fileconf=srcdir + r'\Config', fileexec=srcdir + r'\Executaveis',
                 fileimg=srcdir + r'\Imagens',
                 filedoc=srcdir + r'\Documentos', filecert=srcdir + r'\Certificados', filetest=srcdir + r'\Outros',
                 filejson=srcdir + r'\Json_Xml',
                 filemidias=srcdir + r'\Midias', fileterraform=srcdir + r'\Terraform'
                 ):
        self.filezip = filezip
        self.filepdf = filepdf
        self.filetxt = filetxt
        self.filexlsx = filexlsx
        self.fileconf = fileconf
        self.fileexec = fileexec
        self.fileimg = fileimg
        self.filedoc = filedoc
        self.filecert = filecert
        self.filetest = filetest
        self.filejson = filejson
        self.filemidias = filemidias
        self.fileterraform = fileterraform

    def _move_geral(self, ext, path):
        try:
            os.listdir(path)
            for file in os.listdir(self.srcdir):
                if file.endswith(ext) or file.endswith(ext.upper()):
                    arquivo = file
                    file = os.path.join(self.srcdir, file)
                    try:
                        shutil.move(file, path)
                    except shutil.Error:
                        print(f'Arquivo "{arquivo}" já existe no diretório: {path}.')
        except FileNotFoundError:
            os.mkdir(path)
            self._move_geral(ext, path)

    def cria_pasta(self, pasta):
        pasta = fr'\{pasta}'
        try:
            os.listdir(self.srcdir + pasta)
            print(f'A pasta "{pasta.upper()}" já existe')
        except FileNotFoundError:
            print(f'Criando pasta {pasta.upper()}')
            os.mkdir(self.srcdir + pasta)

    def del_rdp(self):
        for file in os.listdir(self.srcdir):
            if file.endswith('.rdp'):
                file = os.path.join(self.srcdir, file)
                print(f'deletando arquivo {file}')
                os.remove(file)


if __name__ == '__main__':
    a = MoveFile()
    a._move_geral('.txt', r'C:\Users')
