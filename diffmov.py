import shutil
import os
import sys
import stat

__version__ = "0.1"
__filename__ = os.path.basename(sys.argv[0])
__author__ = "licface"
__url__ = "licface@yahoo.com"
__target__ = "all"
__build__ = "2.7"

class DifficultRemove():
    def __init__(self):
        pass

    def on_rm_error(self, func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    def Remove(self, rmdir):
        try:
            shutil.rmtree(rmdir)
        except:
            shutil.rmtree(rmdir,onerror = self.on_rm_error)


if __name__ == "__main__":
    import sys,os
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            main = DifficultRemove()
            main.Remove(sys.argv[1])
        else:
            pass
    else:
        pass