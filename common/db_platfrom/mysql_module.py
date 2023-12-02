# coding:utf-8

import setting
from common.module import config_moudle
from common.module.db_platform.sql_process import SQLBaseDal

log = setting.logging


class Mysql_Module:
    def __init__(self, mysql_url=None):
        """
        连接数据库
        """
        self.ci = config_moudle.ConfigModule().read_config_shizhun_ini()
        if mysql_url is None:
            self.mysql_url = self.ci.get_value("mysql", "mysql_url")
        else:
            # self.mysql_url = parse.quote_plus(mysql_url)
            self.mysql_url = mysql_url
        print('数据库连接：' + self.mysql_url)
        self.sql_dal = SQLBaseDal(mysql_url=self.mysql_url)

    def get_connect_sqldb(self):
        """连接数据库"""
        # self.sql_dal = SQLBaseDal(mysql_url=self.mysql_url)
        return self.sql_dal

    def get_update_excute_sql(self, sql_str):
        """执行update sql_str语句"""
        return self.sql_dal.mysql_pandas.update_by_sql(sql_str)

    def get_excute_sql(self, sql_str):
        """执行sql_str语句"""
        return self.sql_dal.mysql_pandas.query_count_by_sql(sql_str)

    def update_user_login_status(self):
        """更新用户登录状态"""
        sql_str = "UPDATE safe_user_info SET is_online= 0 WHERE loginname='autotester'"
        # sql_str = 'UPDATE {table_name} SET {key}={value} WHERE loginname={username}'.format(
        #     table_name='safe_user_info', key='is_online', value=1, username='autotester')
        self.get_update_excute_sql(sql_str)

    def get_talbe_list(self):
        """返回数据表名列表"""
        return self.sql_dal.mysql_pandas.all_tables()['Tables_in_power_db'].values.tolist()

    def get_df_by_table_name(self, table_name):
        """返回table_name的df """
        return self.sql_dal.mysql_pandas.read_df_by_table_name(table_name)

    def read_df_by_sql(self, sql):
        """按sql语句查询并返回的df """
        return self.sql_dal.mysql_pandas.read_df_by_sql(sql)


    def save_df_to_sql_by_table(self, df, table_name):
        """将df按table_name存储到mysql """
        return self.sql_dal.mysql_pandas.insert_df(df, table_name)

    def delete_df_by_table(self, table_name):
        """清空表table_name """
        return self.sql_dal.mysql_pandas.delete_table(table_name)

    def get_com_date_by_scope_id_table(self, sql=None):
        """从scope_id表格中获取最后一次计算时间"""
        try:
            cc_sql = config_moudle.ConfigModule().read_config_mysql_ini()
            if sql == None:
                sql = cc_sql.get_value('sql_str', 'com_date_latest')
            df = self.sql_dal.mysql_pandas.read_df_by_sql(sql)
            line_num = df.shape[0]
            if line_num != 0:
                com_date = df.iloc[0, 0]
            return str(com_date)

        except Exception as exp:
            print(exp)

    def delete_df_by_value(self, table_name, id, sql_str):
        """删除指定的数据 """
        return self.sql_dal.mysql_pandas.delete_df_by_value(table_name, id, sql_str)



if __name__ == '__main__':
    test_db = Mysql_Module()
    test_db.get_connect_sqldb()
    lsit = test_db.get_talbe_list()
    print(lsit)
    # res = test_db.get_com_date_by_scope_id_table()
    # print(type(res))
    # print(res)
