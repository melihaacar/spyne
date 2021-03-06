
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#


"""The ``spyne.error`` module contains various common exceptions that the user
code can throw.
"""


from spyne.model.fault import Fault
from spyne.const import MAX_STRING_FIELD_LENGTH


class ResourceNotFoundError(Fault):
    """Raised when requested resource is not found."""

    def __init__(self, fault_object,
                                fault_string="Requested resource %r not found"):
        Fault.__init__(self, 'Client.ResourceNotFound',
                                                    fault_string % fault_object)


class InvalidCredentialsError(Fault):
    """Raised when requested resource is not found."""

    def __init__(self, fault_object,
             fault_string="You do not have permission to access this resource"):
        Fault.__init__(self, 'Client.InvalidCredentialsError', fault_string)


class RequestTooLongError(Fault):
    """Raised when request is too long."""

    def __init__(self, faultstring="Request too long"):
        Fault.__init__(self, 'Client.RequestTooLong', faultstring)


class RequestNotAllowed(Fault):
    """Raised when request is incomplete."""

    def __init__(self, faultstring=""):
        Fault.__init__(self, 'Client.RequestNotAllowed', faultstring)


class ArgumentError(Fault):
    """Raised when there is a general problem with input data."""

    def __init__(self, faultstring=""):
        Fault.__init__(self, 'Client.ArgumentError', faultstring)


class InvalidInputError(Fault):
    """Raised when there is a general problem with input data."""

    def __init__(self, faultstring="", data=""):
        Fault.__init__(self, 'Client.InvalidInput', (faultstring, data))


class ValidationError(Fault):
    """Raised when the input stream does not adhere to type constraints."""

    def __init__(self, obj, custom_msg='The value %r could not be validated.'):
        s = repr(obj)

        if len(s) > MAX_STRING_FIELD_LENGTH:
            s = s[:MAX_STRING_FIELD_LENGTH] + "(...)"

        Fault.__init__(self, 'Client.ValidationError', custom_msg % s)


class InternalError(Fault):
    """Raised to communicate server-side errors."""
    def __init__(self, error):
        Fault.__init__(self, 'Server', "InternalError: An unknown error has occured.")
