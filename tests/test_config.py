from Config.LogRecorderConfig import LogRecorderConfig


def test_logRecorder_config():
    log_rec_cfg = LogRecorderConfig()
    log_rec_cfg.parse('../Config/recorder.yml')
    assert int(log_rec_cfg.interval) == 2
    assert log_rec_cfg.extension == "*.log"
