# Copyright 2024 NTILE
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Dev commands."""

import nox


@nox.session(tags=["analyze"], python=False)
def format(session):  # pylint: disable=redefined-builtin
    """Execute addlicense, black and isort."""
    session.run("poetry", "install")
    session.run("addlicense", "-c", "NTILE", "dash_duckdb", "noxfile.py")
    session.run("poetry", "run", "black", "dash_duckdb", "noxfile.py")
    session.run("poetry", "run", "isort", "dash_duckdb", "noxfile.py")


@nox.session(tags=["analyze"], python=False)
def lint(session):
    """Execute linters."""
    session.run("poetry", "install")
    session.run("poetry", "run", "pylint", "dash_duckdb", "noxfile.py")
    session.run("npm", "exec", "markdownlint-cli2", "*.md")
