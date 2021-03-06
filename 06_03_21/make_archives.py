import tempfile
from urllib import request
import mimetypes
import shutil
import time
import os

endpoints = ['https://i.pinimg.com/236x/f0/66/96/f06696bd1d3ea207ce9a83d60ab87486.jpg']
# 'https://www.coolfreecv.com/doc/coolfreecv_resume_en_06_n.docx',

dr = tempfile.TemporaryDirectory(prefix='Temp_', dir='.')
for endpoint in endpoints:
    resp = request.urlopen(endpoint)
    extention = mimetypes.guess_extension(resp.headers['Content-Type'])
    with tempfile.NamedTemporaryFile(prefix='Temp_file', suffix=extention, dir=dr.name, delete=False) as temp_f:
        shutil.copyfileobj(resp, temp_f)

shutil.make_archive('./archived_downloads', 'zip', dr.name)

dr.cleanup()
