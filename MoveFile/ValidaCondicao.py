from ClasseMoveGeral import MoveFile
from pathlib import Path


class Executa(MoveFile):
    def valida(self):
        myset = set()
        src = Path(self.srcdir)
        for file in src.glob('*.*'):
            myset.add(file.suffix)
        return myset

    def condicao(self):
        for i in self.valida():
            if i == '.txt':
                self._move_geral(i, self.filetxt)
            if i == '.docx' or i == '.pptx' or i == '.doc':
                self._move_geral(i, self.filedoc)
            if i == '.xlsx' or i == '.csv':
                self._move_geral(i, self.filexlsx)
            if i == '.zip' or i == '.7z' or i == '.rar' or i == '.gz':
                self._move_geral(i, self.filezip)
            if i == '.jpg' or i == '.jpeg' or i == '.png' or i == '.png'.upper():
                self._move_geral(i, self.fileimg)
            if i == '.pdf':
                self._move_geral(i, self.filepdf)
            if i == '.pem' or i == '.pub' or i == '.pfx':
                self._move_geral(i, self.filecert)
            if i == '.conf':
                self._move_geral(i, self.fileconf)
            if i == '.exe' or i == '.msi':
                self._move_geral(i, self.fileexec)
            if i == '.json' or i == '.xml':
                self._move_geral(i, self.filejson)
            if i == '.mp4':
                self._move_geral(i, self.filemidias)
            if i == '.tf':
                self._move_geral(i, self.fileterraform)
            if i is not None:
                self._move_geral(i, self.filetest)
