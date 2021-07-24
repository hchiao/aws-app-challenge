import unittest
import importlib
import logging
import jsonpickle
import json
from aws_xray_sdk.core import xray_recorder

logger = logging.getLogger()
xray_recorder.configure(
  context_missing='LOG_ERROR'
)

xray_recorder.begin_segment('test_init')
function = __import__('lambda_function')
handler = function.lambda_handler
xray_recorder.end_segment()

class TestFunction(unittest.TestCase):

  def set_event(self, event_file):
    file = open(event_file, 'rb')
    ba = bytearray(file.read())
    event = jsonpickle.decode(ba)
    file.close()
    return event

  def test_event(self):
    xray_recorder.begin_segment('test_function')
    event = self.set_event('event.json')
    logger.warning('## EVENT')
    logger.warning(jsonpickle.encode(event))
    context = {'requestid' : '1234'}
    result = handler(event, context)
    self.assertRegex(str(result), 'FunctionCount', 'Should match')
    xray_recorder.end_segment()

if __name__ == '__main__':
    unittest.main()
