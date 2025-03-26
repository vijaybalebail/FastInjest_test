import oracledb
import threading
import time
import random

# Configuration
DB_CONFIG = {
    "user": "vector",
    "password": "vector",
    "dsn": "localhost/orclpdb1",  # Example: "localhost/orclpdb"
}
THREAD_COUNT = 5
ROWS_PER_THREAD = 100000
USE_FAST_INGEST = True  # Toggle for regular insert vs fast ingest

TABLE_NAME = "test_fast_ingest"


def insert_rows(thread_id, use_hint):
    conn = oracledb.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for i in range(ROWS_PER_THREAD):
        row_id = thread_id * 100000 + i
        value = f"data-{random.randint(1, 9999)}"
        if use_hint:
            sql = f"INSERT /*+ MEMOPTIMIZE_WRITE */ INTO {TABLE_NAME} VALUES (:1, :2)"
        else:
            sql = f"INSERT INTO {TABLE_NAME} VALUES (:1, :2)"
        try:
            cursor.execute(sql, (row_id, value))
            conn.commit()
        except Exception as e:
            print(f"[Thread {thread_id}] Error inserting row {row_id}: {e}")

    cursor.close()
    conn.close()


def run_test(use_hint):
    threads = []
    start_time = time.time()
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=insert_rows, args=(i, use_hint))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end_time = time.time()
    return end_time - start_time


def main():
    print("Running performance test...")

    print("\n[1] Running WITHOUT Fast Ingest...")
    time_regular = run_test(use_hint=False)
    print(f"Time taken (regular inserts): {time_regular:.2f} seconds")

    print("\n[2] Running WITH Fast Ingest...")
    time_fast = run_test(use_hint=True)
    print(f"Time taken (fast ingest): {time_fast:.2f} seconds")

    print("\n🔍 Comparison:")
    print(f"Fast Ingest Speedup: {time_regular / time_fast:.2f}x" if time_fast > 0 else "Error in fast ingest run.")


if __name__ == "__main__":
    main()
