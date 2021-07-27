import unittest
import os
import logging
import jsonpickle
from aws_xray_sdk.core import xray_recorder
from moto import mock_dynamodb2

logger = logging.getLogger()
xray_recorder.configure(
  context_missing='LOG_ERROR'
)
#function = importlib.import_module(lambda_function)

xray_recorder.begin_segment('test_init')
function = __import__('lambda_function')
handler = function.lambda_handler
xray_recorder.end_segment()

@mock_dynamodb2
class TestFunction(unittest.TestCase):

  def test_function(self):
    os.environ['AWS_DEFAULT_REGION']='ap-southeast-2'
    xray_recorder.begin_segment('test_function')
    file = open('create-event.json', 'rb')
    try:

      ba = bytearray(file.read())
      event = jsonpickle.decode(ba)
      logger.warning('## EVENT')
      logger.warning(jsonpickle.encode(event))
      context = {'requestid' : '12345678'}

      result = handler(event, context)

      print(str(result))
      self.assertRegex(str(result), 'Success', 'Should match')

    finally:
      file.close()
    file.close()
    xray_recorder.end_segment()

if __name__ == '__main__':
    unittest.main()
