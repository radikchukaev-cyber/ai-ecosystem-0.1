import pytest
import time
import threading
from queue import Queue

class TestSystemCoordination:
    """Tests coordination between multiple threads/processes."""

    def test_producer_consumer_queue(self):
        """Tests message passing between producer and consumer."""
        message_queue = Queue()
        results = []

        def producer():
            for i in range(5):
                message_queue.put(f"Message {i}")
                time.sleep(0.01)
            message_queue.put(None) # Sentinel

        def consumer():
            while True:
                msg = message_queue.get()
                if msg is None:
                    break
                results.append(msg)
                message_queue.task_done()

        prod_thread = threading.Thread(target=producer)
        cons_thread = threading.Thread(target=consumer)

        prod_thread.start()
        cons_thread.start()

        prod_thread.join()
        cons_thread.join()

        assert len(results) == 5
        assert results[0] == "Message 0"
        assert results[-1] == "Message 4"

    def test_thread_locking(self):
        """Tests standard lock mechanics for shared resources."""
        counter = 0
        lock = threading.Lock()

        def increment():
            nonlocal counter
            for _ in range(100):
                with lock:
                    counter += 1

        threads = [threading.Thread(target=increment) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert counter == 500
