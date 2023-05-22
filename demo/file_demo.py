'''
file upload demo
pip install minio
'''

from minio import Minio

# init minio_client
client = Minio(
    "play.min.io",
    access_key="ACCESS_KEY",
    secret_key="SECRET_KEY",
    secure=True
)

# check is connected
client.bucket_exists("your-bucket-name")

# create bucket
if not client.bucket_exists("your-bucket-name"):
    client.make_bucket("your-bucket-name")

# upload file
try:
    client.fput_object(
        "your-bucket-name",
        "path/to/your/file.ext",
        "/path/to/local/file.ext"
    )
    print("success upload MinIO！")
except Exception as err:
    print(err)

# download file
client.download_file('your-bucket-name', 'file-to-download.txt', 'local-file.txt')
