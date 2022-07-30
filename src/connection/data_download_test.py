from .data_download import DatabaseDownload


def test_download_tables():
    download_tables = DatabaseDownload()
    download_tables.download_tables()
