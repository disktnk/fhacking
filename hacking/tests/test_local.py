# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flake8.api import legacy as flake8
import pycodestyle

import hacking.tests


def check(physical_line):
    """Test check to make sure local-checks are working."""
    if physical_line.strip() == "#this-is-the-test-phrase":
        return (0, "L100: Found local-check test case")


class HackingTestCase(hacking.tests.TestCase):
    def test_local_check(self):
        flake8.get_style_guide(parse_argv=False, ignore='F')
        line = ["#this-is-the-test-phrase"]
        checker = pycodestyle.Checker(lines=line, quiet=True)
        checker.check_all()
        self.assertIn("L100", checker.report.counters)
