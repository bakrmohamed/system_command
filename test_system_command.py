import os
import unittest
from unittest.mock import patch, Mock
import system_command as app

class RunnerTests(unittest.TestCase):
    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            app.parse_command('  ')

    @unittest.skipIf(os.name == 'nt', 'POSIX argument parser')
    def test_quotes_preserved(self):
        self.assertEqual(app.parse_command('echo "two words"'), ['echo', 'two words'])

    def test_no_shell_and_exit_status(self):
        with patch.object(app.subprocess, 'run', return_value=Mock(returncode=3)) as run:
            self.assertEqual(app.run_command('example'), 3)
            self.assertFalse(run.call_args.kwargs['shell'])

    def test_exit_does_not_run(self):
        with patch('builtins.input', return_value='exit'), patch.object(app, 'run_command') as run:
            app.main()
            run.assert_not_called()

    def test_eof_exits(self):
        with patch('builtins.input', side_effect=EOFError), patch.object(app, 'run_command') as run:
            app.main()
            run.assert_not_called()
