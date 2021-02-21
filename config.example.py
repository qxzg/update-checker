# 数据库配置
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 2233,
    'dbname': 'update_checker',
    'username': 'update_checker',
    'password': 'pass',
    'charset': 'utf8mb4'
}
LogFile = "./update-checker.log"
FileLogLevel = "INFO"  # 日志级别，取值：DEBUG，INFO，WARNING，ERROR，CRITICAL
StreamLogLevel = "DEBUG"
LogFormat = "%(asctime)s - %(name)s - [%(levelname)s]: %(message)s"