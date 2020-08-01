import logging  
import time

# 函数式简单配置
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message') 

# 灵活配置日志级别，日志格式，输出位置:
file_handler = logging.FileHandler(filename='E:\\x1.log', mode='a', encoding='utf-8',)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)
logging.error('你好')


# 日志切割
# from logging import handlers
# sh = logging.StreamHandler()
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5)
# fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     handlers=[fh,sh,rh],
#     level=logging.ERROR
# )

# for i in range(1,100000):
#     time.sleep(1)
#     logging.error('KeyboardInterrupt error %s'%str(i))

# logger对象配置
logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf-8') 

# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象 
logger.addHandler(ch) 

logger.debug('logger debug message') 
logger.info('logger info message') 
logger.warning('logger warning message') 
logger.error('logger error message') 
logger.critical('logger critical message')
