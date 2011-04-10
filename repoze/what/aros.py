# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2011, Gustavo Narea <me@gustavonarea.net>.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
Built-in Access Request Objects.

A repoze.what ARO is a callable that takes the request object and returns
a boolean to report whether the requester matches the one it represents.

TODO: Implement ARO for groups once group adapters have been implemented

"""


__all__ = ["ANONYMOUS", "AUTHENTICATED", "UserId"]


AUTHENTICATED = lambda request: bool(request.remote_user)
"""ARO that matches any authenticated user."""


ANONYMOUS = lambda request: not AUTHENTICATED(request)
"""ARO that matches anonymous users."""


class UserId(object):
    """Access Request Object that matches a specific user Id."""
    
    def __init__(self, user_id):
        """
        
        :param user_id: The Id of the expected user.
        
        """
        self.user_id = user_id
    
    def __call__(self, request):
        return request.remote_user == self.user_id