import logging
import datetime
from pytz import timezone
from logging.config import dictConfig



print('---------log start------------')
# # logging.basicConfig(filename = "logs/test.log", level = logging.DEBUG)
# rootlogger = logging.getLogger()
# rootlogger.setLevel(logging.INFO)
# stream_handler = logging.StreamHandler()
# # rootlogger.addHandler(stream_handler)
# rootlogger.info("test------------")

# print("my 로거")
# mylogger = logging.getLogger("my")
# mylogger.setLevel(logging.INFO)
# stream_handler2 = logging.StreamHandler()
# mylogger.addHandler(stream_handler2)
# mylogger.info("-my logger2")
# dictConfig({
#     'version': 1,
#     'formatters': {
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#         }
#     },
#     'handlers': {
#         'file': {
#             'level': 'ERROR', # INFO level 이상의 데이터를 로깅
#             # 로깅 파일이 계속 쌓이지 않도록 특정 용량을 넘으면 가장 오래된 로그가 삭제됨.
#             'class': 'logging.handlers.RotatingFileHandler', 
#             'filename': './logs/test_error.log', # 저장 경로
#             # 'maxBytes': 1,
#             'maxBytes': 1024 * 1024 * 5,  # 5 MB
#             'backupCount': 5,
#             'formatter': 'default',
#             'encoding': 'utf-8'
#         },
#         "console": {
#             "level": "INFO",
#             "class": "logging.StreamHandler",
#             "formatter": "default",
#             "stream": "ext://sys.stdout",
#         },
#         # "email": {
#         #     "class": "logging.handlers.SMTPHandler",
#         #     "formatter": "default",
#         #     "level": "ERROR",
#         #     "mailhost": ("smtp.samsung.net", 25),
#         #     "fromaddr": "hh.k@miracom.co.kr",
#         #     "toaddrs": ["hh.k@miracom.co.kr"],
#         #     "subject": "Error Logs",
#         #     "credentials": ("hh.k", "zaq1xsw2!"),
#         # }
#     },
#     'root': {
#         'level': 'INFO',
#         'handlers': ['file','console']
#         # 'handlers': ['file','console','email']
#     }
# })


def log(request, message):
    log_date = get_log_date()
    log_message = "{0}/{1}/{2}".format(log_date, str(request), message)
    logging.info(log_message)
def error_log(request, error_code, error_message):
    log_date = get_log_date()
    log_message = "{0}/{1}/{2}/{3}".format(log_date, str(request), error_code, error_message)
    logging.info(log_message)

def get_log_date():
    dt = datetime.datetime.now(timezone("Asia/Seoul"))
    log_date = dt.strftime("%Y%m%d_%H:%M:%S")
    return log_date