import subprocess
import logging
import os

try:
    import google.colab
    IN_COLAB = True
except:
    IN_COLAB = False
    
if IN_COLAB:
    print('==='*20)
    print('설치환경: Google Colab')
    print('PyCaret 설치 하는 중입니다. 잠시만 기다려 주세요.\n(설치는 약 1~3분 정도 소요 됩니다)')
    os.environ["PYCARET_CUSTOM_LOGGING_LEVEL"] = "CRITICAL"
    level = os.getenv("PYCARET_CUSTOM_LOGGING_LEVEL", "CRITICAL")
    logger = logging.getLogger('logs')
    logger.setLevel(level)
    # subprocess.run(['pip', 'install', '--pre', 'pycaret'])
    subprocess.run(['pip', 'install', 'pycaret'])
    print('==='*20)
    print('[알림] PyCaret 설치가 완료 되었습니다.')
    print('==='*20)
else:
    print('==='*20)
    print('설치환경: Local')
    print('별도의 PyCaret을 설치하지 않습니다(skip)')
    print('PyCaret의 설치를 진행하려는 경우 다음의 명령어를 실행해 주세요')
    print('!pip install pycaret')
    print('==='*20)
    print('[알림] 완료')
    print('==='*20)