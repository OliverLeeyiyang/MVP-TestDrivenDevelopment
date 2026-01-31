import sqlite3
import os

# 连接到现有的数据库
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'scan_data.db')

print(f"Inspecting database: {db_path}")
print("=" * 60)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 获取所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Tables in database:")
    for table in tables:
        table_name = table[0]
        print(f"- {table_name}")
        
        # 获取表结构
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("  Columns:")
        for column in columns:
            print(f"    {column[1]} ({column[2]})")
        
        # 获取表中的数据行数
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"  Rows: {count}")
        
        # 获取前5行数据作为示例
        print("  Sample data:")
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
        sample_data = cursor.fetchall()
        for row in sample_data:
            print(f"    {row}")
        print()
    
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
print("=" * 60)
