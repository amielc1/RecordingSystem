# import time
#
# import pytest
#
# from Utils.RepeatedTimer import RepeatedTimer
#
# pytest.test_num = 1
#
#
# def increment_num():
#     pytest.test_num += 1
#
#
# def test_tiemr_repeated():
#     timer = RepeatedTimer(1, increment_num)
#     timer.start()
#     time.sleep(3)
#     timer.stop()
#     assert pytest.test_num == 3
