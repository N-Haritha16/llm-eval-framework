from llm_eval.logger import setup_logger

def test_logger():
    logger = setup_logger("test")
    logger.info("hello")
    assert logger is not None
