from unittest import mock
from unittest import TestCase
from click.testing import CliRunner

from . import fixtures

from src.agify import cli
from src.agify.client import NameData
from src.agify.client import AgifyAPIClient


class TestCli(TestCase):
    def test_run(self):
        mock_data = NameData(**fixtures.CLIENT_SUCCESS)
        runner = CliRunner()
        with mock.patch.object(AgifyAPIClient, 'fetch', return_value=mock_data):
            result = runner.invoke(cli.run, [mock_data.name])
            self.assertEqual(result.exit_code, 0)
            self.assertIn(str(mock_data), result.output)