from hashlib import md5
from datetime import date, datetime
from requests import post
from requests_toolbelt.multipart.encoder import MultipartEncoder
from psycopg2 import connect
import pytz


def find_satuan_by_name(conn: connect, nama_satuan: list):
    conn.execute(
        "select id_satuan,nama_satuan from product_satuan where nama_satuan = %s", [nama_satuan])
    return conn.fetchone()


def insert_satuan(conn: connect, payload: list[any]):
    conn.execute(
        "insert into product_satuan (nama_satuan) values (%s) returning id_satuan", payload)
    return conn.fetchone()


def find_status_by_name(conn: connect, nama_status: list):
    conn.execute(
        "select id_status,nama_status from product_status where nama_status = %s", [nama_status])
    return conn.fetchone()


def insert_status(conn: connect, payload: list[any]):
    conn.execute(
        "insert into product_status (nama_status) values (%s) returning id_status", payload)
    return conn.fetchone()


def insert_product(conn: connect, payload: list[any]):
    conn.execute(
        "insert into product_product (id_product,nama_product,harga,kategori_id,status_id,nomor,created_at,updated_at) values (%s,%s,%s,%s,%s,%s,%s,%s) returning id_product", payload)
    return conn.fetchone()


def get_satuan_id(conn: connect, param: list) -> int:
    satuan = find_satuan_by_name(conn, param)
    satuan_id = 0
    if satuan:
        satuan_id = satuan[0]
    else:
        satuan_id = insert_satuan(conn, [param])[0]
    return satuan_id


def get_status_id(conn: connect, param: list) -> int:
    status = find_status_by_name(conn, param)
    status_id = 0
    if status:
        status_id = status[0]
    else:
        status_id = insert_status(conn, [param])[0]
    return status_id


def run_shell():
    hour = datetime.now().hour + 1
    username = f"tesprogrammer{date.today().strftime('%d%m%y')}C{'{:02d}'.format(hour)}"
    password = md5(
        f"bisacoding-{date.today().strftime('%d-%m-%y')}".encode()).hexdigest()
    form_data = MultipartEncoder(
        fields={"username": username, "password": password})
    print(form_data.fields)
    headers = {"Content-Type": form_data.content_type, }
    res = post("https://recruitment.fastprint.co.id/tes/api_tes_programmer",
               headers=headers, data=form_data)
    result = res.json()
    conn = connect(
        "dbname=product_management user=postgres password=1 host=localhost port=5432")
    cursor = conn.cursor()
    utc = pytz.utc
    utc_now = datetime.now(tz=utc)
    if result['error'] == 1:
        print("error")
        return
    else:
        data = result['data']
        for i in data:
            satuan_id = get_satuan_id(cursor, i['kategori'])
            status_id = get_status_id(cursor, i['status'])
            product = insert_product(
                cursor, [i['id_produk'], i['nama_produk'], i['harga'], satuan_id, status_id, i['no'], utc_now, utc_now])
            conn.commit()
            print(product)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    run_shell()
