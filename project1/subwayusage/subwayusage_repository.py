class UsageRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'project1', 'user': 'root', 'password': 'Wnalsrl1210', 'charset': 'utf8' }

    def select_subwayusage_by_name(self, name_key):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = 'select distinct SubLine, SubStation from subway_usage where SubStation like %s'
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall()
        keys = ['SubLine', 'SubStation']
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)
        
        conn.close()

        return result

    def select_subwayusage_by_substation(self, SubStation):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select SubLine, SubStation, pass_on_board, dise_pass from subway_usage where subline = %s"
        cursor.execute(sql, (SubStation,))

        row = cursor.fetchone() # 반환 값은 tuple (...)
        keys = ['SubLine', 'SubStation', 'pass_on_board', 'dise_pass']
        
        result = { key:value for key, value in zip(keys, row) }
            
        conn.close()

        return result