import json


class CSException(Exception):
    pass


class CSError(CSException):
    pass


class AppError(CSError):
    def __init__(self, parameters, traceback):
        self.parameters = json.dumps(parameters, indent=4)
        self.traceback = traceback
        super().__init__(traceback)


class ValidationError(CSError):
    pass


class BadPostException(CSError):
    def __init__(self, errors, *args, **kwargs):
        self.errors = errors
        super().__init__(*args, **kwargs)


class ForkObjectException(CSError):
    pass


class VersionMismatchException(CSError):
    pass


class PermissionExpiredException(CSError):
    pass


class ResourceLimitException(CSException):
    collaborators_msg = (
        "You have reached the limit for the number of collaborators "
        "on private simulations. You may make this simulation public "
        "or upgrade to Compute Studio Plus or Pro to add more "
        "collaborators."
    )

    def __init__(self, resource, test_name, upgrade_to, *args, **kwargs):
        self.resource = resource
        self.upgrade_to = upgrade_to
        self.test_name = test_name
        super().__init__(*args, **kwargs)

    def todict(self):
        return dict(
            resource=self.resource,
            test_name=self.test_name,
            upgrade_to=self.upgrade_to,
            msg=str(self),
        )
