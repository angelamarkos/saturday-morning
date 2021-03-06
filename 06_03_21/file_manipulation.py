from tempfile import NamedTemporaryFile
import shutil
import os
import time
import tempfile
f2 = NamedTemporaryFile(mode='w+t', prefix='Temp_', suffix='.py')
directory = tempfile.TemporaryDirectory(prefix='Tempdir_', dir='.')
directory.cleanup()

print(dir(NamedTemporaryFile))
# time.sleep(15)
print(f2.name)
print(tempfile.gettempdir())
if __name__ == '__main__':
    f3 = NamedTemporaryFile()


class ContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        return open(self.filename, mode=self.mode)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



