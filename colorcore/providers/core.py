# -*- coding: utf-8; -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Flavien Charlon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio


class AbstractBlockchainProvider(object):
    """Represents an abstract class providing access to the Blockchain."""

    @asyncio.coroutine
    def list_unspent(self, addresses, *args, **kwargs):
        """
        Returns the list of unspent transaction outputs for the given addresses.

        :param list[str] addresses: The addresses to query.
        :return: The list of unspent transaction outputs.
        :rtype: list[dict]
        """
        raise NotImplementedError

    @asyncio.coroutine
    def get_transaction(self, transaction_hash, *args, **kwargs):
        raise NotImplementedError

    @asyncio.coroutine
    def sign_transaction(self, transaction, *args, **kwargs):
        raise NotImplementedError

    @asyncio.coroutine
    def send_transaction(self, transaction, *args, **kwargs):
        raise NotImplementedError